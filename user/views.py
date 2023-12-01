from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]
