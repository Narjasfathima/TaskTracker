from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import serializers
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.hashers import check_password
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from Users.api.serializers.taskserializer import TaskListSerializer, TaskUpdateSerializer, TaskReportViewSerializer
from Admin.models import CustomUser, Task
from Users.manager import IsUser, IsAdminOrSuperadmin


class TaskListView(ListAPIView):
    permission_classes = [IsAuthenticated, IsUser]
    serializer_class = TaskListSerializer

    def get(self,request):
        task_list = Task.objects.filter(assigned_to=request.user)
        serializer = TaskListSerializer(task_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TaskStatusUpdateView(APIView):
    permission_classes = [IsAuthenticated, IsUser]  
    
    @swagger_auto_schema(
        request_body=TaskUpdateSerializer,
        responses={
            201: openapi.Response("Task Status updated"),
            400: openapi.Response('Bad Request', TaskUpdateSerializer),
        }
    )

    def put(self, request, pk, format=None):    
        task_instance = Task.objects.get(id=pk)
        serializer = TaskUpdateSerializer(task_instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Successfully updated"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    

class TaskReportView(APIView):
    permission_classes = [IsAuthenticated, IsAdminOrSuperadmin]
    serializer_class = TaskReportViewSerializer

    def get(self, request, pk, format=None):
        task_instance = Task.objects.get(id=pk)
        serializer = self.serializer_class(task_instance, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
        