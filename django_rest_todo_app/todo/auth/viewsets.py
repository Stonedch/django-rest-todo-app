from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

from .serializers import LoginSerializer, RegistrationSerializer

class LoginViewSet(ModelViewSet):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])


class RegisterViewSet(ModelViewSet):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny, )
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        return Response({
            'user': serializer.data,
            'refresh': res['refresh'],
            'token': res['access'],
        }, status=status.HTTP_201_CREATED)


class RefreshViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except InvalidToken as e:
            raise InvalidToken(e.args[0])

        return Response(serializer.validated_data, status=HTTP_200_OK)
