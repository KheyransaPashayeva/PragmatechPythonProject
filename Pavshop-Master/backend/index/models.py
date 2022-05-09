from django.db import models
from django.utils import timezone
# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=220)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    message = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname
