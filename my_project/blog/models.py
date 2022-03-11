from django.db import models
from distutils.command.upload import upload
# Create your models here.
class Post(models.Model):

    STATUS_CHOICES = (
        ('deactive', 'Deactive'),
        ('active', 'Active'),
    )

    title = models.CharField(max_length=127,blank=False, null=False)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=70, default='Admin')
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/',null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    views = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-published_date', )

    def __str__(self):
        return f'{self.author}\'s Post -{self.title}'