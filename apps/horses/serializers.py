from rest_framework import serializers as s

from apps.horses.models import User, HorseImage


class HorseImageSerializer(s.ModelSerializer):
    class Meta:
        model = HorseImage
        fields = ('id', 'user', 'image')


class HorseSerializer(s.ModelSerializer):
    # user_images = HorseImageSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'password')


class HorseProfileSerializer(s.ModelSerializer):
    email = s.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'birth_day', 'weight', 'examined_at')

    # def validate_email(self, value):
    #     lower_email = value.lower()
    #     if User.objects.filter(email__iexact=lower_email).exists():
    #         raise s.ValidationError("This email is already taken")
    #     return lower_email


class RegistrationSerializer(s.ModelSerializer):
    password = s.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'password')

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        if validated_data['password']:
            user.set_password(validated_data['password'])
        user.save()
        return user
