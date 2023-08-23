from django.db import models;
# import movipy.editor


class Admin(models.Model):
    full_name= models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='Admin_Profile')
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "1. Admin"

    def __str__(self):
        return self.full_name


class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='Profile_Pics', blank=True)
    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "2. User"

    def __str__(self):
        return self.first_name


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
    content = models.TextField()
    remarks = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "5. Content"
        
    def __str__(self):
        return str(self.blogs)


