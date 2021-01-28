from rest_framework import viewsets

from usermanager.models import CustomUser
from usermanager.serializer import UserSerializer


class RegisterUser(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        return False
