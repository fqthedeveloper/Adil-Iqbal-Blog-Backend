from django.contrib import admin
from . import models
# Register your models here.



admin.site.register(models.Admin)

class UsersAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name')

admin.site.register(models.Users, UsersAdmin)


class CategoryAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'description')

admin.site.register(models.Category, CategoryAdmin)


class BlogsAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'author', 'updated_on')

admin.site.register(models.Blogs, BlogsAdmin)


class ContentAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'blogs')

admin.site.register(models.Content, ContentAdmin)

