from django.db import models

from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from home.utils import unique_slug_generator




class TopicModel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'topics'



class PostModel(models.Model):
    topic = models.ForeignKey(TopicModel, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=140)
    slug = models.SlugField(max_length=142, unique=True)
    body = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'posts'
        


class MuseumModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='artworks'
        get_latest_by = ['date']



def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)
    
pre_save.connect(slug_save, sender=PostModel)