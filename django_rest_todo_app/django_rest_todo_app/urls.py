from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from todo.urls import router as todo_router
from todo.user.urls import router as user_router

router = routers.DefaultRouter()

router.registry.extend(todo_router.registry)
router.registry.extend(user_router.registry)

urlpatterns = router.urls

urlpatterns = [
    path('api/', include(router.urls), name='api'),
]
