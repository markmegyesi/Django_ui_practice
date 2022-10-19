from django.urls import path
from .views import home, about, contact
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView,
                    PostUpdateView,
                    PostDeleteView


                    )
from .models import PostsModel
urlpatterns = [
    path('about/',about, name='blog-about') ,
    path('contact/',contact, name='blog-contact') ,
    # path('',home, name='blog-home') ,
    path('',PostListView.as_view(), name='blog-home') ,
    path('post/<int:pk>/',PostDetailView.as_view(), name='post-detail') ,
    path('post/<int:pk>/update/',PostUpdateView.as_view(), name='post-update') ,
    path('post/new/',PostCreateView.as_view(), name='post-create') ,
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name='post-delete')
]
