from django.db import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, BlogsSerializer, ContentSerializer, AdminSerializer, LikeSerializer, CommentSerializer
from rest_framework import generics
from . import models
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated



class AdminList(generics.ListCreateAPIView) :
    queryset = models.Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classese = [permissions.IsAuthenticated]


class adminDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Users.objects.all()
    serializer_class = AdminSerializer
    permission_classese = [permissions.IsAuthenticated]


@csrf_exempt
def admin_login(request) :
    email = request.POST['email']
    password = request.POST['password']

    try :
        adminData = models.Admin.objects.get(email=email, password=password)

    except models.Admin.DoesNotExist :
        adminData = None

    if adminData :
        return JsonResponse({'bool' :True, 'user_id' :adminData.id})
    else :
        return JsonResponse({'bool' :False})

class AdminBlogsList(generics.ListCreateAPIView) :
    serializer_class = ContentSerializer

    def get_queryset(self) :
        author_id = self.kwargs['author_id']
        author = models.Admin.objects.get(pk=author_id)
        return models.Content.objects.filter(author=author)



class UsersList(generics.ListCreateAPIView):
    queryset = models.Users.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        # Check if the username already exists
        if models.Users.objects.filter(username=request.data.get('username')).exists():
            return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)

        # Validate and save the user
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({'message': 'User  created successfully.', 'user_id': user.id}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def User_login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        user = models.Users.objects.get(email=email)
    except models.Users.DoesNotExist:
        return Response({'bool': False}, status=status.HTTP_401_UNAUTHORIZED)

    if user.check_password(password):
        return Response({'bool': True, 'user_id': user.id})
    else:
        return Response({'bool': False}, status=status.HTTP_401_UNAUTHORIZED)

class UsersDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Users.objects.all()
    serializer_class = UserSerializer


class CategoryList(generics.ListCreateAPIView) :
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class BlogsList(generics.ListCreateAPIView):
    serializer_class = BlogsSerializer

    def get_queryset(self):
        qs = models.Blogs.objects.all()

        # Filter by category if provided
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            qs = qs.filter(category__name__icontains=category)  # Assuming 'name' is the field in Category model

        # Order by updated_on descending (most recent updates first)
        qs = qs.order_by('-updated_on', '-id')

        # Limit the results if 'result' parameter is provided
        if 'result' in self.request.GET:
            limit = int(self.request.GET['result'])
            qs = qs[:limit]

        return qs

    def post(self, request):
        serializer = BlogsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

class BlogsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blogs.objects.all()
    serializer_class = BlogsSerializer

class ContentList(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Content.objects.all()
    serializer_class = ContentSerializer


class BlogsContentList(generics.ListCreateAPIView):
    serializer_class = ContentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        blogs_id = self.kwargs['blogs_id']
        blogs = models.Blogs.objects.get(pk=blogs_id)
        return models.Content.objects.filter(blogs=blogs)


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user) 


class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        content_id = self.kwargs['content_id']
        return models.Comment.objects.filter(content_id=content_id)