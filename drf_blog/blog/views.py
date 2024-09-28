from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView


from .models import Blog, Category, Comment
from .serializers import BlogSerializer, CategorySerializer, CommentSerializer
from .pagination import ListPagination


class BlogListView(generics.ListCreateAPIView):
    # queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    pagination_class = ListPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "subtitle", "id"]

    permission_classes = [IsAuthenticated]

    throttle_classes = [UserRateThrottle]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes  = [IsAuthenticated]

    def get_queryset(self):
        
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog=blog_id)
    
    def perform_create(self, serializer):
        blog_id = self.kwargs['blog_id']
        user =  self.request.user 
        blog = Blog.objects.get(id=blog_id)
        serializer.save(author=user, blog=blog)
