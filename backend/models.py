from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(null=False , unique=True)
    date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=255)

    def __str__(self):
        return self.name
