from django.db import models
from autenticacao.models import Usuario

class Post(models.Model):
    user = models.ForeignKey(Usuario,on_delete=models.CASCADE,blank = True,null = True) 
    titulo = models.CharField(max_length = 30,blank = False)
    descricao = models.CharField(max_length =100,blank = False)
    imagem = models.ImageField(upload_to = 'imagens',verbose_name='Imagem Post', null= True,blank= True)
    
    def __str__(self):
        return self.titulo