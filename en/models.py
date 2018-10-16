from django.db import models
from django.utils import timezone




class TopicModel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'topics'






class PostModel(models.Model):
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=140)
    body = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'posts'