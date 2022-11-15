from rest_framework import serializers
from users.models import UserRegister

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserRegister
        fields = ['name', 'surnames', 'email', 'phone', 'hobbies']