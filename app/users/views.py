from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer, AuthTokenSerializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


class CreateUserView(CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializers

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
