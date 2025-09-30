from django.shortcuts import render
from .models import Post   # import your Post model

# Home page view
def home(request):
    return render(request, "blog/home.html")

# Post list view
def post_list(request):
    posts = Post.objects.all().order_by("-published_date")  # newest first
    return render(request, "blog/post_list.html", {"posts": posts})