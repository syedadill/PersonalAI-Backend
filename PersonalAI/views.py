from django.shortcuts import render
# Create your views here.
from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny , IsAuthenticated
from django.contrib.auth.models import User
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from .models import *

class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

    


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
from AIAssistant.settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

@csrf_exempt
def ai_response(request):
    if request.method == "POST":
        user_data = {
            "assets": 5000,  # Replace with actual user data
            "income": 3000,
            "expenses": 2000,
        }
        query = request.POST.get("query")

        prompt = f"""
        You are a personal assistant. Here is the user's financial data:
        Assets: ${user_data['assets']}
        Income: ${user_data['income']}
        Expenses: ${user_data['expenses']}

        The user asked: {query}
        """

        try:
            # Use the new API syntax
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # or any other model you are using
                prompt=prompt,
                max_tokens=150
            )

            return JsonResponse({"response": response.choices[0].text.strip()})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
