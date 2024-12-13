# urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, OnboardingAPIView
# from PersonalAI.views import ai_response
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # JWT Token URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),   
    # User Registration and Profile URLs
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileDetailView.as_view(), name='profile'),
    # path('ai-response/', ai_response, name='ai_response'),
    path('onboarding/', OnboardingAPIView.as_view(), name='onboarding'),
]