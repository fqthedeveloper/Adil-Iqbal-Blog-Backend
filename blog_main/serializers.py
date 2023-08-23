from rest_framework import serializers
from . import models
from django.contrib.auth.hashers import make_password



class AdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Admin
        fields = ['id','full_name', 'email', 'password', 'profile_pic']
        depth=1


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Users
        fields = ['id','first_name', 'last_name', 'email', 'password', 'profile_pic']
        depth=1



class CategorySerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.Category
        fields = ['id','title', 'description']


class BlogsSerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.Blogs
        fields = ['id', 'category', 'title', 'futher_image', 'author', 'updated_on', 'content', 'created_on', 'blogs_content']
        depth=1


class ContentSerializer(serializers.ModelSerializer) :
    class Meta :
        model = models.Content
        fields = ['id', 'blogs', 'title', 'content', 'video', 'remarks']