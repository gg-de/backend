from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class UserView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]

    @api_view(['POST'])
    def register(request):
        email = request.data.get('email')
        password = request.data.get('password')
        fullname = request.data.get('fullname')
        if not email or not password:
            return JsonResponse(status=500)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )
        token = Token.objects.create(user=user)
        return JsonResponse(status=200, data={'token': token.key})
