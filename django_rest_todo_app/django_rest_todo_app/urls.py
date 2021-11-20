"""django_rest_todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from todo import views
from todo.auth.viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet
from todo.user.viewsets import UserViewSet

router = routers.DefaultRouter()

router.register('tasks/?', views.TaskView, 'task')

# Authentication routers
router.register('auth/login', LoginViewSet, 'auth-login')
router.register('auth/register', RegistrationViewSet, 'auth-register')
router.register('auth/refresh', RefreshViewSet, 'auth-refresh')

# User routers
router.register('user/', UserViewSet, 'user')

slashless_router = routers.DefaultRouter(trailing_slash=False)
slashless_router.registry = router.registry[:]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(slashless_router.urls)),
]
