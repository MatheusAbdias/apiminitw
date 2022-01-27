from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed

from datetime import timedelta
from django.utils import timezone
from django.conf import settings

# Referencia desse arquivo: https://medium.com/@yerkebulan199/django-rest-framework-drf-token-authentication-with-expires-in-a05c1d2b7e05

#Retorna o tempo que falta para expirar o token
def expires_in(token):
    time_elapsed = timezone.now() - token.created
    left_time = timedelta(seconds = 8600) - time_elapsed
    return left_time

#Verifica se o token expirou  ou não
def is_token_expired(token):
    return expires_in(token) < timedelta(seconds = 0)

# se o token esta espirando um novo token é estabelecido
# se o token esta espirado ele tem que ser removido
# e um novo token sera criado

def token_expire_handler(token):
    is_expired = is_token_expired(token)
    if is_expired:
        token.delete()
        token = Token.objects.create(user = token.user)
    return is_expired, token


#________________________________________________
#DEFAULT_AUTHENTICATION_CLASSES
class ExpiringTokenAuthentication(TokenAuthentication):
    """
    Se token esta espirado então ele é romovido
    e novo token com uma nova key é criada
    """
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key = key)
        except Token.DoesNotExist:
            raise AuthenticationFailed("Invalid Token")
        
        if not token.user.is_active:
            raise AuthenticationFailed("User is not active")

        is_expired, token = token_expire_handler(token)
        if is_expired:
            raise AuthenticationFailed("The Token is expired")
        
        return (token.user, token)