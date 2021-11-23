from django.urls import path, include

from rest_framework import routers

from .views import TaskView

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'tasks/?', TaskView, 'tasks')
