from django.shortcuts import render
from rest_framework.views import APIView
from postagem.serializer import PostSerializer
from .models import Post
from rest_framework import status,generics,parsers
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

class PostUsuarioViewSet(APIView):
    '''Retorna uma lista de post do sistema ou adiciona um novo post do usuario'''
    permission_classes = (IsAuthenticated,)
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    def get(self,request,format=None):
        queryset = Post.objects.order_by("-id").exclude(user = self.request.user)[:10]
        serializer = PostSerializer(queryset, many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ListaPostsViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset
    serializer = PostSerializer

        
