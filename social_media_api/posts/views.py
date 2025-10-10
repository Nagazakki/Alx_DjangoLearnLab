from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Like
from notifications.utils import create_notification
from .serializers import LikeSerializer

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if created:
        create_notification(
            actor=request.user,
            recipient=post.author,
            verb='liked your post',
            target=post
        )

    serializer = LikeSerializer(like)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    like = Like.objects.filter(user=request.user, post=post).first()

    if like:
        like.delete()
        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)