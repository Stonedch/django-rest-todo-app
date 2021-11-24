from django.urls import path, include

from rest_framework import routers

from .viewsets import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet, 'users')
