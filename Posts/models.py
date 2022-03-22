from django.db import models
from django.utils.text import slugify
from accounts.models import User
import datetime
from tinymce.models import HTMLField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, blank=False, null=False, unique=True)
    content = HTMLField()
    thumbnail = models.ImageField(upload_to='thumbnails')
    cdn_url = models.CharField(max_length=350)
    slug = models.SlugField(null=True, blank=True)
    create_date = models.DateField(auto_now_add=True)
    publish_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        else:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def publish(self):
        self.publish_date = datetime.datetime.now()
        self.save()
