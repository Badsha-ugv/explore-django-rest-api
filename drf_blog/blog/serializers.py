from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from .models import Blog, Category, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField (read_only=True)
    class Meta:
        model = Blog
        fields = ['title', 'subtitle', 'details', 'author']

    # def create(self, validated_data):
    #     user = self.context['request'].user
    #     return Blog.objects.create(author=user, **validated_data)
    # def create(self, validated_data):
    #     # author = self.context['request'].user
    #     # return Blog.objects.create(author=author, **validated_data)
    #     user = self.request.user
    #     print('uuuuu', user)

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ['title', 'details','author']

