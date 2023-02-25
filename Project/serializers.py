from rest_framework import serializers
from uploadimage.models import Image
from django.contrib.auth.models import User
from .models import UserTier

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Image
        fields = ['id', 'image', 'thumbnail_200', 'thumbnail_400', 'original_image', 'expiring_link']
        read_only_fields = ['thumbnail_200', 'thumbnail_400', 'original_image', 'expiring_link']

    def create(self, validated_data):
        image = Image.objects.create(image=validated_data['image'])
        image.generate_thumbnail()
        image.generate_expiring_link()
        return image


class UserTierSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTier
        fields = '__all__'