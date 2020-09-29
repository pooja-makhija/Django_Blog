from rest_framework import serializers
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id", "title", "content", "status", "user_id", "created_at", "updated_at"]

class UpdateBlogStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["id","status"]

