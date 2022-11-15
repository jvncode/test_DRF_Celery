from django.urls import path
from users.views import User_APIView, Profile_APIView


urlpatterns = [
    path(f'api/v1/signup', User_APIView.as_view(), name='new_user'),
    path(f'api/v1/profile/<int:pk>', Profile_APIView.as_view(), name='profile_user'),
]
