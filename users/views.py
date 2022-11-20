import os

from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import AllowAny

from .models import Profile
from .serializers import ProfileSerializers, UserSerializer
from users import tasks
from dotenv import load_dotenv

load_dotenv()


class ProfileView(RetrieveAPIView):
    serializer_class = ProfileSerializers
    http_method_names = ['get']

    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user


class UserCreateAPIView(CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        if os.environ.get('APP_ENV', default='') == 'PROD':
            tasks.send_mail.delay(request.data['email'])
            tasks.send_sms.delay(request.data['phone'])
        return super().post(request, *args, **kwargs)
