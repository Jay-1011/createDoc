from django.urls import path
from .views import UserRegistrationAPIView, UserLoginAPIView, UserDetailAPIView

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('detail/', UserDetailAPIView.as_view(), name='user-detail'),
]
