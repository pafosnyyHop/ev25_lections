from rest_framework import generics, permissions
from django.contrib.auth.models import User
from dj_rest_auth.views import LoginView, AllowAny, LogoutView
from . import serializers


class CustomLoginView(LoginView):
    permission_classes = (permissions.AllowAny,)


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.RegisterSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    permissions_classes = (permissions.IsAuthenticated,)


class UserDetailViews(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserDetailSerializer
    permissions_classes = (permissions.IsAuthenticated,)

