from rest_framework import routers

from .viewsets import LoginViewSet, RegistrationViewSet, RefreshViewSet

router = routers.DefaultRouter(trailing_slash=True)

router.register(r'auth/login', LoginViewSet, basename='auth-login')
router.register(r'auth/register', RegistrationViewSet, basename='auth-register')
router.register(r'auth/refresh', RefreshViewSet, basename='auth-refresh')


urlpatterns = [
]
