from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = (
            'avatar',
            'user_bg',
            'name',
            'position',
            'description',
            'email',
            'phone',
            'workPhone',
            'instagram',
            'facebook',
            'twitter',
            'telegram',
            'linkedin',
            'youtube',
            'whatsapp',
            'behance',
            'other_link',
            'unique_id'
        )