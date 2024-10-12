# features/notifications.py
from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def get_notifications():
    return Notification.objects.all()
