from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from blog_api import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('posts/', views.BlogPostList.as_view()),
    path('posts/<int:pk>/', views.BlogPostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
