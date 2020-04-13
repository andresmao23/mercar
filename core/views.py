from django.shortcuts import render, HttpResponse
from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from .serializers import ClientSerializer, ClientUserSerializer, ClientDetailSerializer, StoreSerializer
from .models import Client, Store
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.core import serializers

# Create your views here.

class ClientDetailList(generics.ListAPIView):
    serializer_class = ClientDetailSerializer
    def get_queryset(self):
        client_id = self.kwargs['id']
        return Client.objects.filter(id=client_id)

class StoreDetail(generics.ListAPIView):
    serializer_class = StoreSerializer
    def get_queryset(self):
        client_id = self.kwargs['client_id']
        return Store.objects.filter(client_id=client_id)

class ClientViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUserList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientUserSerializer

    def post(self, request, *args, **kwargs):
        clients = []
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            client = Client.objects.get(user_id=user.id)
            clients.append(client)
            data = serializers.serialize('json', clients)
            return HttpResponse(data, content_type="application/json")
        return Response(status=status.HTTP_400_BAD_REQUEST)

class Register(generics.CreateAPIView):
    def post(self, request, *args, **kwargs):
        # Información para crear el usuario
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        #print('************** ENTRANDO AL METODO ************')
        #print(username)
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        # Información para crear el cliete
        cedula = request.POST.get('cedula')
        name = request.POST.get('name')
        first_lastname = request.POST.get('first_lastname')
        second_lastname = request.POST.get('second_lastname')
        phone = request.POST.get('phone')
        client = Client.objects.create(user=user, cedula=cedula, name=name, first_lastname=first_lastname, second_lastname=second_lastname, phone=phone)
        client.save()
        # Información para crear el establecimiento
        return Response({'respuesta':'Usuario creado satisfactoriamente!', 'Id_usuario':user.id})
