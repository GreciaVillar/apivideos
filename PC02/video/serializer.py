from rest_framework import serializers
from .models import TipoDeVideo, Alquiler, Cliente

class TipoDeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeVideo
        fields= ['id','nombre','descripcion','categoria','precio_alquiler','image','url']

class AlquilerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alquiler
        fields = ['id', 'video_alquilado', 'cliente', 'fecha_alquiler', 'fecha_devolucion']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nombre','direccion','numero_telefono','correo_electronico']