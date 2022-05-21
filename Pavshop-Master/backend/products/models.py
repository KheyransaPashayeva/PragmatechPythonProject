from django.db import models
from distutils.command.upload import upload
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.utils import timezone
# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/',null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=300,blank=True,null=True,unique=True)
    
      
    def get_absolute_url(self):
       return reverse_lazy('products:product_detail', kwargs={'slug':self.slug})

    def save(self):
      super(Products,self).save()
      self.slug = slugify(self.name + str(self.published_date))
      print(self.published_date)
      return super(Products,self).save()

    def __str__(self):
        return self.name