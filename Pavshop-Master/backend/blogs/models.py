from django.db import models
from distutils.command.upload import upload
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    total = models.IntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='blogposts/',null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(max_length=300,blank=True,null=True,unique=True)
    
    def get_absolute_url(self):
       return reverse_lazy('blogs:blog_detail', kwargs={'slug':self.slug})

    def save(self):
      super(Blog,self).save()
      self.slug = slugify(self.title + str(self.published_date))
      print(self.published_date)
      return super(Blog,self).save()

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=120)
    

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=220)
    email = models.EmailField(max_length=120)
    subject = models.CharField(max_length=120)
    text = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE,related_name="comments",null=True)

    def __str__(self):
        return self.name
