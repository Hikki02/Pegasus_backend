import os

from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.users.models import User
from apps.users.serializers import UserSerializer
import vobject


class UserMVC(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'unique_id'

    def create(self, request, *args, **kwargs):
        user = User.objects.get(key=request.data['key'])

        if user.unique_id.__str__() == kwargs[self.lookup_field]:
            return Response(data={'message': 'ok'})
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        user = User.objects.get(key=request.data['key'])

        if user.unique_id.__str__() == kwargs[self.lookup_field].strip():
            serializer = self.serializer_class(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class DownloadVCF(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'unique_id'

    def retrieve(self, request, *args, **kwargs):
        user = self.queryset.filter(unique_id=kwargs['unique_id']).first()
        user = self.serializer_class(user).data
        socials = [
            ('facebook', user['facebook'] or '',),
            ('instagram', user['instagram'] or '',),
            ('youtube', user['youtube'] or '',),
            ('behance', user['behance'] or '',),
            ('twitter', user['twitter'] or '',),
            ('telegram', user['telegram'] or '',),
            ('whatsapp', user['whatsapp'] or '',),
            ('linkedin', user['linkedin'] or '',),
            ('other_link', user['other_link'] or '',)
        ]
        vCard = vobject.vCard()

        vCard.add('fn').value = user['name']
        vCard.add('email').value = user['email'] or ''
        vCard.email.type_param = 'INTERNET'

        vCard.add('tel').value = f"+{user['phone']}" or ''
        vCard.tel.type_param = 'CELL'

        workPhone = vCard.add('tel')
        workPhone.value = f"+{user['workPhone']}" or ''
        workPhone.type_param = 'WORK'

        for social in socials:
            soc = vCard.add('url')
            soc.type_param = social[0]
            soc.value = social[1]

        with open(f'{user["name"].replace(" ", "_")}.vcf', 'a') as file:
            file.write(vCard.serialize())

        file = open(f'{user["name"].replace(" ", "_")}.vcf', 'r').read()

        response = HttpResponse(file, content_type='application/text')
        response['Content-Disposition'] = f'attachment; filename={user["name"].replace(" ", "_")}.vcf'

        os.remove(f"{user['name'].replace(' ', '_')}.vcf")

        return response