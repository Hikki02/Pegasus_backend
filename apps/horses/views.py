from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.response import Response

from apps.horses.models import Horse
from apps.horses.serializers import (
    HorseSerializer, )
from apps.horses.utils import generateError, generateAuthInfo


class UserLoginView(generics.CreateAPIView):
    queryset = Horse.objects.all()
    serializer_class = HorseSerializer

    def create(self, request, *args, **kwargs):
        uniqueId = request.data.get('uniqueId');
        password = request.data.get('password');
        try:
            user = Horse.objects.get(uniqueId=uniqueId)
        except Horse.DoesNotExist:
            return Response(**generateError('DOES_NOT_EXIST'));
        checkPassword = check_password(password, user.password);
        if not checkPassword:
            return Response(**generateError('WRONG_PASSWORD'));
        serializer = self.serializer_class(user, context={'request': request});
        return Response(data=generateAuthInfo(user, serializer.data));
