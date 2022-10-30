from Livros.models import Livros, Perfil_leitor
from rest_framework import serializers
from django.contrib.auth.models import User

class Livros_serializer(serializers.ModelSerializer):
    class Meta:
        model= Livros
        fields = '__all__'

class Perfil_serializer(serializers.ModelSerializer):
    class Meta :
        models = Perfil_leitor
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','password']