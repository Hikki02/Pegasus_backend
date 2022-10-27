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


class HorseProfileSerializer(s.Serializer):
    id = s.IntegerField(read_only=True)
    name = s.CharField(max_length=225, required=True)
    email = s.EmailField(required=True)
    birth_day = s.DateField(required=True)
    weight = s.IntegerField(required=True)
    examined_at = s.DateField(required=True)

    def validate_email(self, value):
        lower_email = value.lower()
        if User.objects.filter(email__iexact=lower_email).exists():
            raise s.ValidationError("email should be unique")
        return lower_email

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.birth_day = validated_data.get('birth_day', instance.birth_day)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.examined_at = validated_data.get('examined_at', instance.examined_at)
        instance.save()
        return instance
