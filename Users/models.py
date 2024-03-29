from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.functions import TransactionNow
from django.utils import timezone
import datetime


class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="static/images/default.jpg",
        upload_to="static/images/",
        height_field=None,
        width_field=None,
        max_length=100,
    )
    profile_blurb = models.TextField(blank=True)


class GramPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(
        upload_to="static/images/",
        height_field=None,
        width_field=None,
        max_length=100,
    )
    blurb = models.TextField()
    time = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(GramPost, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


class PostComments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(GramPost, on_delete=models.CASCADE)
    comment = models.TextField()
