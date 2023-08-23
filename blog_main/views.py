from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, CategorySerializer, BlogsSerializer, ContentSerializer, AdminSerializer
from rest_framework import generics
from rest_framework import permissions
from . import models
from webbrowser import get
from datetime import datetime



class AdminList(generics.ListCreateAPIView) :
    queryset = models.Admin.objects.all()
    serializer_class = AdminSerializer
    #permission_classese = [permissions.IsAuthenticated]


class adminDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Users.objects.all()
    serializer_class = AdminSerializer
    #permission_classese = [permissions.IsAuthenticated]


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



class UsersList(generics.ListCreateAPIView) :
    queryset = models.Users.objects.all()
    serializer_class = UserSerializer
    #permission_classese = [permissions.IsAuthenticated]


class UsersDetail(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Users.objects.all()
    serializer_class = UserSerializer
    #permission_classese = [permissions.IsAuthenticated]

    def get_queryset(self) :
       user_id = self.kwargs['user_id']
       user = models.Users.objects.get(pk=user_id)
       return models.Users.objects.filter(Users=user)


@csrf_exempt
def User_login(request) :
    email = request.POST['email']
    password = request.POST['password']

    try :
        userData = models.Users.objects.get(email=email, password=password)

    except models.Users.DoesNotExist :
        userData = None

    if userData :
        return JsonResponse({'bool' :True, 'user_id' :userData.id})
    else :
        return JsonResponse({'bool' :False})


class CategoryList(generics.ListCreateAPIView) :
    queryset = models.Category.objects.all()
    serializer_class = CategorySerializer


class BlogsList(generics.ListCreateAPIView) :
    queryset = models.Blogs.objects.all()
    serializer_class = BlogsSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if 'result' in self.request.GET:
            limit = int(self.request.GET['result'])
            qs = models.Blogs.objects.all().order_by('-id')[:limit]
       
        if 'category' in self.request.GET:
            category = self.request.GET['category']
            qs = models.Blogs.objects.filter(techs__icontains=category)

        return qs

    def post(self, request):
        print(request.POST)
        serializer = BlogsSerializer(data=request.POST)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)

class BlogsDetailViwe(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Blogs.objects.all()
    serializer_class = BlogsSerializer


class ContentList(generics.RetrieveUpdateDestroyAPIView) :
    queryset = models.Content.objects.all()
    serializer_class = ContentSerializer



class BlogsContentList(generics.ListCreateAPIView) :
    serializer_class = ContentSerializer

    def get_queryset(self) :
        blogs_id = self.kwargs['blogs_id']
        blogs = models.Blogs.objects.get(pk=blogs_id)
        return models.Content.objects.filter(blogs=blogs)
    


# class BlogsDetailViwe(generics.RetrieveUpdateDestroyAPIView) :
#     queryset = models.Blog.objects.all()
#     serializer_class = BlogSerializer