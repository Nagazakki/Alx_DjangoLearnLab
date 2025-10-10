from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from .models import Post, Comment, Like
from django.shortcuts import get_object_or_404, redirect
from notifications.models import Notification
from .serializers import PostSerializer, CommentSerializer
from django.contrib.auth.decorators import login_required
from notifications.utils import create_notification


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission: Only allow owners to edit or delete.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions for safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions only for the owner
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        # Get all users that this user follows
        following_users = user.following.all()

        # Retrieve posts made by those users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    """Allow authenticated users to like a post."""
    post = get_object_or_404(Post, id=post_id)

    # Prevent duplicate likes
    if Like.objects.filter(post=post, user=request.user).exists():
        return Response({'detail': 'You already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create like
    Like.objects.create(post=post, user=request.user)

    # Create notification for the post author
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb="liked your post",
            target=post
        )

    return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    """Allow authenticated users to unlike a post."""
    post = get_object_or_404(Post, id=post_id)
    like = Like.objects.filter(post=post, user=request.user).first()

    if not like:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    like.delete()
    return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)

@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if not Like.objects.filter(user=request.user, post=post).exists():
        Like.objects.create(user=request.user, post=post)
        create_notification(
            actor=request.user,
            recipient=post.author,
            verb='liked your post',
            target=post
        )

    return redirect('post_detail', pk=post.id)  # adjust this to your actual post detail view name


@login_required
def unlike_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.filter(user=request.user, post=post).delete()
    return redirect('post_detail', pk=post.id)