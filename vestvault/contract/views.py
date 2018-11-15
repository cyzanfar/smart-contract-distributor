from rest_framework import generics
from contract.models import Token, Holder
from rest_framework import permissions
from contract.serializers import TokenSerializer, HolderSerializer, \
    UserSerializer

from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TokenList(generics.ListCreateAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class TokenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Token.objects.all()
    serializer_class = TokenSerializer

class HolderList(generics.ListCreateAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer

    def perform_create(self, serializer):
        serializer.save(token=self.request.token)

class HolderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Holder.objects.all()
    serializer_class = HolderSerializer
