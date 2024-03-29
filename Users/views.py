from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, GramPostForm, CommentForm, LikeForm, SiteUserForm
from django.contrib import messages
from .models import SiteUser, GramPost, PostComments, PostLikes
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy


def home(request):
    grampost = GramPost.objects.all().order_by("-time")
    comments = PostComments.objects.all()
    siteuser = SiteUser.objects.all()
    postlikes = PostLikes.objects.all()

    if "heart" in request.POST:
        post_id = request.POST.get("heart")
        post = GramPost.objects.get(id=post_id)
        like_check = PostLikes.objects.filter(
            user=request.user, post=post, like=True
        ).first()
        if like_check == None:
            new_like = PostLikes.objects.create(user=request.user, post=post, like=True)
            new_like.save()
            post.likes += 1
            post.save()
        else:
            like_check.delete()
            post.likes -= 1
            post.save()
        return HttpResponse(f"{post.likes} Likes")

    context = {
        "grampost": grampost,
        "comments": comments,
        "siteuser": siteuser,
        "postlikes": postlikes,
    }
    return render(request, "home.html", context)


def create_user(request):
    errors = ""
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            SiteUser.objects.create(user=user)
            login(request, user)
            return redirect("/profile/")
        else:
            errors = dict(form.errors)
            errors = errors.values()
            print(type(errors))
    else:
        form = SignUpForm()
    return render(request, "create_user.html", {"form": form, "errors": errors})


def makeUser(request):
    if request.method == "POST":
        form = UserCreationForm()
        if form.is_valid():
            form.save()
            return render(request, "create_user.html")
        else:
            form = UserCreationForm()
        return render(request, "create_user.html", {"form": form})


def view_profile(request):
    grampost = GramPost.objects.filter(user=request.user)
    siteuser = SiteUser.objects.all()
    context = {
        "user": request.user,
        "siteuser": siteuser,
        "grampost": grampost,
    }
    return render(request, "profile.html", context)


def edit_profile(request):
    form = SiteUserForm(request.FILES, instance=request.user)
    if "update" in request.POST:
        form = SiteUserForm(request.POST, request.FILES, instance=request.user.siteuser)
        if form.is_valid():
            print("form was valid")
            form.save()
        return redirect("/profile/")
    context = {"user": request.user, "form": form}
    return render(request, "edit_profile.html", context)


def create_post(request):
    if request.method == "POST":
        form = GramPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("/profile/")
        else:
            print(f"there were some errors: {form.errors}")

    else:
        form = GramPostForm()
    return render(request, "create_post.html", {"form": form})


def edit_post(request, pk):
    grampost = GramPost.objects.get(pk=pk)
    form = GramPostForm(instance=grampost)
    if "update" in request.POST:
        form = GramPostForm(request.POST, instance=grampost)
        if form.is_valid():
            form.save()
        return redirect("/profile/")
    if "delete" in request.POST:
        grampost.delete()
        return redirect("/profile/")
    return render(request, "edit_post.html", {"form": form, "post": grampost})


def comment(request, pk):
    grampost = GramPost.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = grampost
            form.save()
            return redirect("/")
    return render(request, "comment.html", {"grampost": grampost, "form": form})
