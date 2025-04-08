from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password

from Users.api.serializers.authserializer import LoginSerializer, LogoutSerializer
from Admin.models import CustomUser, Task
from Users.manager import IsUser


class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def check_user_password(self, user, password):
        return check_password(password, user.password)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            return Response({'message': 'Invalid input data', 'errors': e.detail}, status=status.HTTP_400_BAD_REQUEST)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        if not CustomUser.all_objects.filter(username=username, user_type='User').exists():
            return Response({'message': 'Invalid Username'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = CustomUser.all_objects.get(username=username, user_type='User')
        
        if not self.check_user_password(user, password):
            return Response({'message': 'Invalid Password'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not user.is_active:
            user.is_active = True
            user.save()

        refresh = RefreshToken.for_user(user)

        data = {"access_token": str(refresh.access_token),
                "refresh_token": str(refresh)
                }
        
        return Response(data, status=status.HTTP_200_OK)
    


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        data = response.data
        data['access_token'] = data.pop('access')
        return Response(data)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated, IsUser]
    serializer_class = LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            refresh_token = serializer.validated_data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logout successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response({"message": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Something went wrong. please try again"}, status=status.HTTP_400_BAD_REQUEST)