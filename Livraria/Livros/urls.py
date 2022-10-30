"""Livraria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#importaçoes padroes
from django.urls import path
from .api import views

#importtançao para midia
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('livros/', views.LivroViews.as_view()),
    path('livros/<str:pk>', views.LivroDetails.as_view()),
    path('perfis', views.PerfilView.as_view() ),
    path('perfis/<str:pk>', views.PefilDetails.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/', views.UserView.as_view())
    
]
urlpatterns = urlpatterns+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)