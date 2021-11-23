from rest_framework import viewsets, filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [BasicAuthentication]

    @action(detail=False, methods=['get'])
    def current(self, request: Request):
        queryset = request.user
        serializer = self.get_serializer(queryset, many=False)
        return Response(serializer.data)
