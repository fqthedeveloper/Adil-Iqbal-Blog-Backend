from django.db import models;
from django.contrib.auth.models import AbstractUser , Group, Permission;


class Admin(models.Model):
    full_name= models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='Admin_Profile')
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "1. Auther"

    def __str__(self):
        return self.full_name


class Users(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)  # Example of an additional field
    mobile_no = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='Profile_Pics', blank=True)
    

    class Meta:
        verbose_name_plural = "2. Users"

    def __str__(self):
        return self.first_name

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change this to something unique
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change this to something unique
        blank=True,
    )

    def __str__(self):
        return self.username


class Category(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "3. Category"

    def __str__(self):
        return self.title


class Blogs(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Admin, on_delete= models.CASCADE, related_name='author')
    title = models.CharField(max_length=100, unique=True)
    futher_image = models.ImageField(upload_to='Blog_Images', null=True)
    content = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)


    class Meta:
        verbose_name_plural = "4. Blogs"

    def __str__(self):
        return self.title

    

class Content(models.Model):
    blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE,related_name='blogs_content')
    title = models.CharField(max_length=200, unique=True)
    video = models.FileField(upload_to='Blog_Videos', null=True)
    photo = models.ImageField(upload_to='Blog_Photos', null=True)

    content = models.TextField()
    remarks = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "5. Content"
        
    def __str__(self):
        return str(self.blogs)


class Like(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        unique_together = ('user', 'content')
        verbose_name_plural = "6. Like"

    def __str__(self):
        return f"{self.user} likes {self.content}"

class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "7. comments"

    def __str__(self):
        return f"{self.user} commented on {self.content}"