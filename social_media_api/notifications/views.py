from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(recipient=request.user).order_by('-timestamp')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})