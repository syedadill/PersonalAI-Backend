# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, ChatWithAssistant, UploadFile #ProfileDetailView , EducationViewSet, WorkViewSet, FamilyRelationshipViewSet
# from PersonalAI.views import ai_response
from rest_framework.authtoken.views import obtain_auth_token


# # Initialize the router
# router = DefaultRouter()

# # Register the ProfileViewSet with the router
# router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    # JWT Token URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),   
    # User Registration and Profile URLs
    path('register/', RegisterView.as_view(), name='register'),
    # path('profile/', ProfileDetailView.as_view(), name='profile'),
    # path('ai-response/', ai_response, name='ai_response'),
    # path('education/<int:pk>/', EducationViewSet.as_view(), name='education'),
    # path('work/<int:pk>/', WorkViewSet.as_view(), name='work'),
    # path('family/<int:pk>/', FamilyRelationshipViewSet.as_view(), name='family'),
    path('chat/', ChatWithAssistant.as_view(), name='chat_with_assistant'),
    path('upload/', UploadFile.as_view(), name='upload_file'),
    # path('profiles/', ProfileDetailView.as_view(), name ='profiles')
]