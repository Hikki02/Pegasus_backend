from django.db import IntegrityError
from django.db.models import F
from rest_framework import serializers as s
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

# from .models import Refund, RefundPhoto, CartItem, Cart
# from .models.user_model import User
# from .settings import Email
# from ..comments.serializers import UserCommentSerializer
# from ..products.base import BaseCatalogSerializer, BaseSerializer
# from ..products.models import Catalog


# class RegistrationSerializer(s.ModelSerializer):
#     password = s.CharField(max_length=128, min_length=8, write_only=True)
#     password2 = s.CharField(write_only=True)
#     email = s.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = 'id', 'email', 'username', 'password', 'password2',
#
#     def validate(self, attrs) -> dict[str, str]:
#         password, password2 = attrs.get('password', None), \
#                               attrs.pop('password2', None)
#         if password != password2:
#             raise s.ValidationError({'error': "Пароли не совподают"})
#         return attrs
#
#     def save_and_checking_for_uniqueness(self, user: User) -> None:
#         try:
#             user.save()
#         except IntegrityError:
#             raise ValidationError({
#                 'error': 'Уже такой юзер существует'
#             })
#
#     def _send_email(self, user: User) -> None:
#         email = Email(user)
#         email.send()
#
#     def create_user_cart(self, user: User) -> None:
#         Cart.objects.create(user=user)
#         return ...
#
#     def create(self, validated_data) -> dict:
#         password = validated_data.pop('password')
#         user = User(**validated_data)
#         user.set_password(password)
#         self.save_and_checking_for_uniqueness(user)
#         self.create_user_cart(user)
#         self._send_email(user)
#         return validated_data
#
#
# class EmailVerificationSerializer(s.ModelSerializer):
#     token = s.CharField(max_length=555)
#
#     class Meta:
#         model = User
#         fields = 'token',
#
#
# class ResetPasswordEmailRequestSerializer(s.Serializer):
#     email = s.EmailField(min_length=2)
#
#     redirect_url = s.CharField(max_length=500, required=False)
#
#     class Meta:
#         fields = 'email',
#
#
# class UserSerializer(s.ModelSerializer):
#     password = s.CharField(min_length=8, required=False, write_only=True)
#     password2 = s.CharField(min_length=8, required=False, write_only=True)
#
#     class Meta:
#         model = User
#         fields = 'id', 'email', 'username', 'phone', 'avatar', \
#                  'birth_day', 'gender', 'password', 'password2'
#
#     def validate(self, attrs):
#         password = attrs.get('password', None)
#         password2 = attrs.pop('password2', None)
#         if password != password2:
#             raise ValidationError({'error': 'Пароли не совподают'})
#         return attrs
#
#     def update(self, instance, validated_data):
#         password = validated_data.pop('password', None)
#         if password:
#             instance.set_password(password)
#         super().update(instance, validated_data)
#         return validated_data
#
#
# class ProductSerializer(BaseCatalogSerializer):
#     class Meta:
#         ref_name = 'product'
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         try:
#             data['image'] = instance.product_catalog[0].product_image[0].image
#         except:
#             pass
#         return data
#
#
# class FavoriteCreateSerializer(s.Serializer):
#     catalog_id = s.IntegerField(required=True)
#
#     def get_user(self):
#         return self.context.get('request').user
#
#     def create(self, validated_data):
#         user = self.get_user()
#         catalog_id = validated_data['catalog_id']
#         user.favorites.add(catalog_id)
#         Catalog.objects.filter(id=catalog_id).update(popular=F('popular') + 1)
#         return validated_data
#
#
# class RefundPhotoBaseSerializer(s.Serializer):
#     photo = s.ImageField(read_only=True)
#
#
# class RefundPhotoSerializer(RefundPhotoBaseSerializer):
#     photo = s.ImageField(required=True)
#
#     class Meta:
#         ref_name = 'photo'
#
#
# class RefundCreateSerializer(s.FileField, s.Serializer):
#     product_id = s.IntegerField(required=True)
#     description = s.CharField(required=True)
#
#     photos = RefundPhotoSerializer(many=True, write_only=True, required=True)
#
#     def get_user(self):
#         return self.context.get('request').user
#
#     def save_to_validate_date(self, validate_data, **kwargs):
#         validate_data |= kwargs
#         return validate_data
#
#     def create(self, validated_data):
#         photos = validated_data.pop('photos')
#         user = self.get_user()
#         self.save_to_validate_date(validated_data, user=user)
#         refund = Refund.objects.create(**validated_data)
#         RefundPhoto.objects.bulk_create(
#             [RefundPhoto(refund=refund, photo=i['photo']) for i in photos]
#         )
#         return validated_data
#
#
# class RefundPhotoSerializer(RefundPhotoBaseSerializer):
#     ...
#
#
# class RefundListSerializer(s.Serializer):
#     id = s.IntegerField(read_only=True)
#     description = s.CharField(read_only=True)
#     created_at = s.DateTimeField(read_only=True)
#     status = s.CharField(read_only=True)
#     photos = RefundPhotoSerializer(many=True)
#
#
# """User cart Serializers"""
#
#
# class CartSerializers(s.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = (
#             'id', 'user', 'created_at', 'updated_at',
#         )
#
#
# class CartItemSerializers(s.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = (
#             'id', 'product', 'qt', 'cart'
#         )
#
#
# class BaseUser(s.Serializer):
#     avatar = s.ImageField()
#     username = s.CharField()
#
#     def create(self, validated_data): ...
#
#     def update(self, instance, validated_data): ...
#
#
# class UserCommentsSerializer(s.Serializer):
#     id = s.IntegerField()
#     user = BaseUser()
#     description = s.CharField()
#     created_at = s.DateTimeField()
#     likes = s.IntegerField()
#
#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         try:
#             data['image'] = instance.product.product_catalog.first().product_image.first().image.url
#         except:
#             pass
#         return data
#
#     def create(self, validated_data):
#         ...
#
#     def update(self, instance, validated_data):
#         ...
from apps.horses.models import User, HorseImage


class HorseImageSerializer(s.ModelSerializer):
    class Meta:
        model = HorseImage
        fields = ('user', 'image')

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #
    #     horse_image = HorseImage.objects.create(**validated_data)
    #     if len(horse_image) > 4:
    #         return 'You can create only 4 image'
    #     else:
    #         return horse_image


class HorseSerializer(s.ModelSerializer):
    # user_images = HorseImageSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'password']
