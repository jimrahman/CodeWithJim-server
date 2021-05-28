from rest_framework import generics
from blog_api import serializers
from django.contrib.auth.models import User
from blog_api.models import BlogPost


# Create your views here.
class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = serializers.BlogPostSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
