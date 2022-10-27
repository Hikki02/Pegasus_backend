from django.contrib.auth.hashers import check_password
from django.db.models import Count
from rest_framework import generics
# from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from apps.horses.models import User, HorseImage
from apps.horses.serializers import (
    HorseSerializer, HorseImageSerializer, HorseProfileSerializer)
from apps.horses.utils import generateError, generateAuthInfo


class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = HorseSerializer

    def create(self, request, *args, **kwargs):
        id = request.data.get('id')
        password = request.data.get('password')
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response(**generateError('DOES_NOT_EXIST'))
        checkPassword = check_password(password, user.password)
        if not checkPassword:
            return Response(**generateError('WRONG_PASSWORD'))
        serializer = self.serializer_class(user, context={'request': request})
        return Response(data=generateAuthInfo(user, serializer.data))


class HorseImageListCreate(generics.ListCreateAPIView):
    queryset = HorseImage.objects.filter()
    serializer_class = HorseImageSerializer

    def create(self, request, *args, **kwargs):
        if len(HorseImage.objects.annotate(pk=Count('user')).filter(user=self.request.user)) >= 4:
            raise ValidationError("You can set only 4 images")
        else:
            return super().create(request, *args, **kwargs)


class HorseImageRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HorseImage.objects.filter()
    serializer_class = HorseImageSerializer


class HorseProfileListCreate(generics.ListCreateAPIView):
    queryset = User.objects.filter()
    serializer_class = HorseProfileSerializer


class HorseProfileRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = HorseProfileSerializer