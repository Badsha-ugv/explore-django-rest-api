from django.urls import path 
from . import views 


urlpatterns = [
    path('list/', views.BlogListView.as_view(),name='blog-list'),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(),name='blog-detail'),

    path('blog/<int:blog_id>/comment/', views.CommentView.as_view(), name='comment'),


]