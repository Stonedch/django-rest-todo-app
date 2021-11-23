from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]
