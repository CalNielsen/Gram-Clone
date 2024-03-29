from django.urls import path
from . import views

urlpatterns = [
    path("makeuser", views.makeUser, name="makeuser"),
    path("create_user/", views.create_user, name="create_user"),
    path("profile/", views.view_profile, name="profile"),
    path("create_post", views.create_post, name="create_post"),
    path("<int:pk>/edit_post", views.edit_post, name="edit_post"),
    path("<int:pk>/comment", views.comment, name="comment"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
]
