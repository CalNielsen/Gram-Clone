from django.contrib import admin
from .models import SiteUser, GramPost, PostLikes

# Register your models here.
admin.site.register(SiteUser)
admin.site.register(GramPost)
admin.site.register(PostLikes)
