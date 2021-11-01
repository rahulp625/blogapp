from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

STATUS = (
    (0,"Unpublish"),
    (1,"Publish")
)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Post(models.Model):
    title=models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    content=models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    # status = models.IntegerField(choices=STATUS, default=0)
    published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogs')