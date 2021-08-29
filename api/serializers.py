from .models import *
from rest_framework import fields, serializers

from datetime import date


class ExtraInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraInfo
        fields = ['direccion', 'telefono', 'fechaNacimiento']

# creacion y modificacion de Data en Json anidado
class UsuarioSerializer(serializers.ModelSerializer):
    extraInfo = ExtraInfoSerializer(required=False)

    class Meta:
        model = Usuario
        fields = ['id', 'name', 'email', 'password', 'extraInfo']

    def create(self, validated_data):
        if validated_data.get('extraInfo') is None:
            usuario = Usuario.objects.create(**validated_data)
            return usuario

        extraInfoData = validated_data.pop('extraInfo')
        usuario = Usuario.objects.create(**validated_data)
        ExtraInfo.objects.create(usuario=usuario, **extraInfoData)
        return usuario

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)

        if validated_data.get('extraInfo') is None:
            return instance

        extraInfoData = validated_data.pop('extraInfo')
        ExtraInfo.objects.filter(usuario=instance.id).delete()
        ExtraInfo.objects.create(usuario=instance, **extraInfoData)
        return instance


class UsuarioListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'name', 'email']

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['direccion'] = instance.extraInfo.direccion
        repr['telefono'] = instance.extraInfo.telefono
        repr['fechaNacimiento'] = instance.extraInfo.fechaNacimiento
        hoy = date.today()
        nacimiento = instance.extraInfo.fechaNacimiento
        repr['edad'] = hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))

        return repr
