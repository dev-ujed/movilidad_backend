from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import datetime
from .models import User, UserToken

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        # Validar si el correo pertenece al dominio ujed.mx
        if not email.endswith('@ujed.mx'):
            raise exceptions.AuthenticationFailed("Only users with @ujed.mx can login")

        # Buscar al usuario por correo electrónico
        user = User.objects.filter(email=email).first()

        # Si el usuario no existe, lanzar excepción
        if user is None:
            raise exceptions.AuthenticationFailed('Authentication failed')

        # Verificar que la contraseña sea correcta
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Invalid credentials')

        # Crear el token de acceso y de refresco (usando simplejwt)
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        # Almacenar el token de refresco en la base de datos si es necesario
        UserToken.objects.create(
            user_id=user,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )

        # Crear la respuesta y agregar la cookie del refresh token
        response = Response()
        response.set_cookie(key='refresh_token', value=refresh_token, httponly=True)

        # Regresar el token de acceso (JWT) como respuesta
        response.data = {
            'token': access_token
        }

        return response

class LogoutApiView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')

        # Asegúrate de llamar a la función delete() para eliminar el token
        UserToken.objects.filter(token=refresh_token).delete()

        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'success'
        }

        return response
