from django.contrib import admin
from postagem.models import Post

class Postagens(admin.ModelAdmin):
    '''Possibilita um admin registrar um Postagem'''
    list_display = ('id','titulo','user')
    list_display_links = ('id','titulo')
    search_fields = ('titulo',)
    list_per_page = 10
admin.site.register(Post,Postagens)
