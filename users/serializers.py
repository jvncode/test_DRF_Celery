from rest_framework import serializers
from users.models import Profile


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['name', 'surnames', 'email',
                  'phone', 'hobbies', 'verified_email', 'verified_phone']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('name', 'surnames', 'email', 'phone', 'hobbies')

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.save()
        return user
