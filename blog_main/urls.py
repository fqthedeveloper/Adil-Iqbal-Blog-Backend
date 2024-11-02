from django.urls import path
from . import views

urlpatterns = [
    # admin url 
    path('admin/', views.AdminList.as_view()),

    path('admin/<int:pk>/', views.adminDetail.as_view()),

    path('admin-login', views.admin_login),

    path('author-blogs/<int:author_id>', views.AdminBlogsList.as_view()),

    # user url 

    path('user/', views.UsersList.as_view()),

    path('user/<int:pk>', views.UsersDetail.as_view()),

    path('user-login', views.User_login),

    # Blogs url

    path('category/', views.CategoryList.as_view()),

    path('blogs/', views.BlogsList.as_view()),
    
    path('blogs/<int:pk>', views.BlogsDetailView.as_view()),

    path('content-blogs/<int:blogs_id>', views.BlogsContentList.as_view()),

    path('content/<int:pk>', views.ContentList.as_view()),

    path('blogdetails/<int:pk>', views.BlogsDetailView.as_view()),
    
    path('likes/', views.LikeCreateView.as_view(), name='like-create'),
    
    path('comments/<int:content_id>/', views.CommentListCreateView.as_view(), name='comment-list-create'),
]
