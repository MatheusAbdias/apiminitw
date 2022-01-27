from autenticacao.models import Usuario
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .serializer import LogaUsuarioSerializer, UsuarioSerializer
from rest_framework import generics,status
from rest_framework.response import Response
from django.contrib.auth import get_user_model,authenticate,login
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .Authentication import token_expire_handler,expires_in

class ListaUsuarioViewSet(generics.ListAPIView):
    '''Lista de usuarios Cadastros no Banco'''
    
    permission_classes = (AllowAny,)
    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    serializer_class = UsuarioSerializer

class UsuarioCadastroViewSet(generics.CreateAPIView):
    '''Views Responsavel pelo cadastro'''

    permission_classes = (AllowAny,)
    model = get_user_model()
    serializer_class = UsuarioSerializer


class LogaUsuarioViewSet(APIView):

    permission_classes = (AllowAny,)
    def post(self, request, format=None):

        userLog = LogaUsuarioSerializer(data = request.data)
    
        if not userLog.is_valid():
            
            return Response(userLog.errors,status= status.HTTP_400_BAD_REQUEST)
    
        user = authenticate(
            username = userLog.data['username'],
            password = userLog.data['password']
        )

        if not user:
            return Response({'Detail':'Usuario ou senha invalidos.'},status=status.HTTP_404_NOT_FOUND)
        
        userSerializer = LogaUsuarioSerializer(user)

        #Token
        login(request,user)
        token, _ = Token.objects.get_or_create(user = user)

        is_expired, token = token_expire_handler(token)

        return Response({
            'user' : userSerializer.data,
            'expires_in': expires_in(token),
            'token': token.key
        }, status=status.HTTP_200_OK)

# Responsável pelo logou
class Logout(APIView):

    permission_classes = (AllowAny,)
    def get(self, request, format=None):
        # Apaga o token ativo
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
