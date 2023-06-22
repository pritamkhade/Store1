from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    audio = models.FileField(upload_to='notes/audio/', blank=True)
    video = models.FileField(upload_to='notes/video/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_notes')
