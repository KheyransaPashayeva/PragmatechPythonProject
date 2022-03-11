from django.db import models

from distutils.command.upload import upload
# Create your models here.
class User(models.Model):

    STATUS_CHOICES = (
        ('deactive', 'Deactive'),
        ('active', 'Active'),
    )

    name = models.CharField(max_length=127,blank=False, null=False)
    surname = models.CharField(max_length=70)
    body = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/',null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ('-published_date', )

    def __str__(self):
        return f'User {self.name}'