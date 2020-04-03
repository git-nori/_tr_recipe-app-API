from rest_framework import generics, authentication, permissions
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


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.TokenAuthentication,)

    # get_queryset => 複数件取得時など
    # get_object => １件取得時など
    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user
