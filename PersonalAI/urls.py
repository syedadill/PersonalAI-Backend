# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ProfileDetailView

urlpatterns = [
    # JWT Token URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # User Registration and Profile URLs
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileDetailView.as_view(), name='profile'),
]