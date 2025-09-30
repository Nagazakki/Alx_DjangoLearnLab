from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),          # Home page
    path("posts/", views.post_list, name="post_list"),  # Post list page
]