import email
from rest_framework import serializers
from autenticacao.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style = {'input_type':'password'},
        write_only = True,
        label = 'Senha'
    )

    password_confirm = serializers.CharField(
        style = {'input_type':'password'},
        write_only = True,
        label ="Confirme  a Senha"
    )
    class Meta:
        model = Usuario
        fields =('username','email','password','password_confirm')
        extra_kwarg = {'password':{'write_only':True}}

    def save(self):
        '''cadastro de usuario no banco de dados'''
        conta = Usuario(
            username = self.validated_data['username'],
            email = self.validated_data['email']
        )
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({'password':'As senhas não são iguais.'})
        conta.set_password(password)
        conta.save()
        return conta

class LogaUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)

