from django.db import models
from django.utils import timezone
from django.urls import reverse
from django_imgur.storage import ImgurStorage
# Create your models here.

STORAGE = ImgurStorage()

class Post(models.Model):
    isTemple = models.BooleanField(default=False)
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    tagline =  models.CharField(max_length=200,null=True, blank=True)
    text = models.TextField()
    likes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='photos', storage=STORAGE, null=True, blank=True)
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment = True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE,)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text
