from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import TipoDeVideo, Alquiler, Cliente
from .serializer import TipoDeVideoSerializer, AlquilerSerializer, ClienteSerializer

class TipoDeVideoListView(APIView):
    def get(self, request):
        tipos_de_video = TipoDeVideo.objects.all()
        serializer = TipoDeVideoSerializer(tipos_de_video, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TipoDeVideoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TipoDeVideoDetailView(APIView):
    def get(self, request, tipo_video_id):
        tipo_de_video = get_object_or_404(TipoDeVideo, pk=tipo_video_id)
        serializer = TipoDeVideoSerializer(tipo_de_video)
        return Response(serializer.data)


class AlquilerListView(APIView):
    def get(self, request):
        alquileres = Alquiler.objects.all()
        serializer = AlquilerSerializer(alquileres, many=True)
        return Response(serializer.data)


class AlquilerDetailView(APIView):
    def get(self, request, alquiler_id):
        alquiler = get_object_or_404(Alquiler, pk=alquiler_id)
        serializer = AlquilerSerializer(alquiler)
        return Response(serializer.data)


class ClienteListView(APIView):
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)


class ClienteDetailView(APIView):
    def get(self, request, cliente_id):
        cliente = get_object_or_404(Cliente, pk=cliente_id)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)
