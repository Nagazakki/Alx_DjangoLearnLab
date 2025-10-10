from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView
from . import views

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
    path('like/<int:pk>/', views.like_post, name='like_post'),      # use 'pk' to match checker
    path('unlike/<int:pk>/', views.unlike_post, name='unlike_post'),# use 'pk' to match checker
]