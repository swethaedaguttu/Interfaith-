# features/content_curation.py
from django.db import models

class Content(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

def get_curated_content():
    return Content.objects.all()