from rest_framework import serializers
from django.contrib.auth.models import User
from blog_api.models import BlogPost


class UserSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'posts']


class BlogPostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'body', 'owner']
