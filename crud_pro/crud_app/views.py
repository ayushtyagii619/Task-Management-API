from django.http import Http404
from .models import NewUser,Task
from .serializers import RegisterSerializer,LoginSerializer,TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

def get_token(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }
class RegisterApiView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Registration Complete"},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
    def post(self,request):
        serailizer = LoginSerializer(data=request.data)
        if serailizer.is_valid():
            email = serailizer.data.get('email')
            password = serailizer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                token = get_token(user)
                return Response({"token":token,"msg":"Login Successful"},status=status.HTTP_200_OK)
            return Response({"msg":"email and password doesn't match"},status=status.HTTP_404_NOT_FOUND)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

def get_task_object(pk):
    try:
        return Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        raise Http404

class CreateTaskApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TaskListApiView(APIView):
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'priority']  # Allow filtering by status and priority
    ordering_fields = ['due_date', 'priority']

    def filter_queryset(self, queryset):
        # Filtering
        status_filter = self.request.query_params.get('status')
        priority_filter = self.request.query_params.get('priority')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        if priority_filter:
            queryset = queryset.filter(priority=priority_filter)

        # Sorting
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)

        return queryset
    def get(self,request):
        tasks = Task.objects.all()
        filtered_tasks = self.filter_queryset(tasks)
        serializer = TaskSerializer(filtered_tasks,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class TaskListByIdApiView(APIView):
    def get(self,request,id):
        tasks = get_task_object(id)
        serializer= TaskSerializer(tasks)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class TaskUpdateApiView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,id):
        tasks = get_task_object(id)
        serializer = TaskSerializer(tasks,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TaskDeleteApiView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id):
        task = get_task_object(id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    