from django import forms

from .models import GramPost, PostComments, PostLikes, SiteUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SiteUserForm(forms.ModelForm):
    class Meta:
        model = SiteUser
        fields = ["profile_pic", "profile_blurb"]


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            "username",
            "password1",
            "password2",
        )


class GramPostForm(forms.ModelForm):
    class Meta:
        model = GramPost
        fields = ["image", "blurb"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ["comment"]


class LikeForm(forms.ModelForm):
    class Meta:
        model = PostLikes
        fields = ["like"]
