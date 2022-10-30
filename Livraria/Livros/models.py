from asyncio.windows_events import NULL
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Livros (models.Model):
    nome_do_livro = models.CharField(max_length=250, blank = False)
    capa = models.ImageField(upload_to="profile_images", default='blank-profile-picture.png')
    #TODO consertar esse erro : django.db.utils.IntegrityError:
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(max_length=100, null = False, blank = False)
    isbn = models.BigIntegerField( null = False, blank = False)
    locador = models.ForeignKey(User, on_delete=models.CASCADE)


class Perfil_leitor (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    bio = models.TextField(max_length=100)
    profileimg = models.ImageField(upload_to="profile_images",default='blank-profile-picture.png')
    location = models.CharField(max_length=100, blank=True)