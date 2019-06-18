from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers.users import UserSerializer
from api.models import User


class UserView(ModelViewSet):
    serializer_class= UserSerializer
    queryset = User.objects.all()

