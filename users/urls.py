from django.urls import path
from users.views import ProfileView, UserCreateAPIView


urlpatterns = [
    path('api/v1/signup', UserCreateAPIView.as_view(), name='new_user'),
    path('api/v1/profile', ProfileView.as_view(), name='profile_user'),
]
