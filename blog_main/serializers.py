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
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'mobile_no', 'password')
        extra_kwargs = {
            'password': {'write_only': True}  # Ensure the password is write-only
        }

    def create(self, validated_data):
        user = models.Users(
            username=validated_data['username'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            email=validated_data.get('email', ''),
            mobile_no=validated_data.get('mobile_no', '')
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user



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
        fields = ['id', 'blogs', 'title', 'content', 'photo', 'video', 'remarks']
        depth=2


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Like
        fields = ['id', 'user', 'content']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'user', 'content', 'text', 'created_on']
        depth=1