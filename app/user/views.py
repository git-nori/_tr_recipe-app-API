from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from .serialize import UserSerializer, AuthTokenSerializer
from rest_framework.settings import api_settings


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    # settings.pyのDEFAULT_RENDERER_CLASSESをセット
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
