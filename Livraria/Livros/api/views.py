import re
from .serializers import Livros_serializer, Perfil_serializer, UserSerializer
from Livros.models import Livros, Perfil_leitor
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework import generics

class LivroViews(APIView):

    def get(self, request, format=None):
        livro = Livros.objects.all()
        serializer = Livros_serializer(livro, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Livros_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PerfilView(APIView):

    def get (self, request, format=None):
        perfil = Perfil_leitor.objects.all()
        serializer = Perfil_serializer(perfil, many=True)
        return Response(serializer.data)

    def post (self, request, format=None):
        serializer = Perfil_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):

    def get (self, request, format=None):
        perfil = User.objects.all()
        serializer = UserSerializer(perfil, many=True)
        return Response(serializer.data)


    def post (self, request, format=None):
        serializer =UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LivroDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Livros.objects.get(pk=pk)
        except Livros.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        livro = self.get_object(pk)
        serializer = Livros_serializer(livro)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        livro = self.get_object(pk)
        serializer = Livros_serializer(livro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        livro = self.get_object(pk)
        livro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class PefilDetails(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Perfil_leitor.objects.get(pk=pk)
        except Perfil_leitor.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = Perfil_serializer(perfil)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        perfil = self.get_object(pk)
        serializer = Perfil_serializer(perfil, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        perfil = self.get_object(pk)
        perfil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)