from codecs import backslashreplace_errors
from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = models.CharField(max_length = 40,unique=True,error_messages={'unique':"O nome de usuario já esta cadastrado"})
    userDescricao = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=254, unique=True,error_messages={'unique':"O email cadastrado já existe."})
    userFollows = models.ManyToManyField('self',blank =True,symmetrical=True)
    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.username

