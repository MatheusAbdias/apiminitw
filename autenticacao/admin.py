from django.contrib import admin
from autenticacao.models import Usuario

class Usuarios(admin.ModelAdmin):
    '''Possibilita um admin registrar um Usuario'''
    list_display = ('id','username','email')
    list_display_links = ('id','username')
    search_fields = ('username',)
    list_per_page = 10

admin.site.register(Usuario,Usuarios)
