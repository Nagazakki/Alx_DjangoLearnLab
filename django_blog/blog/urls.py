from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import CommentCreateView, PostByTagListView

urlpatterns = [
    path("", views.home, name="home"),
    path("posts/", views.post_list, name="post_list"),

    # Authentication
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="registration/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # CRUD for posts
    path("post/new/", views.PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post/<int:pk>/update/", views.PostUpdateView.as_view(), name="post_update"),
    path("post/<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),

    # Comments CRUD
    path("post/<int:post_pk>/comments/new/", views.comment_create, name="comment_create"),
    path("post/<int:post_pk>/comments/<int:pk>/edit/", views.CommentUpdateView.as_view(), name="comment_update"),
    path("post/<int:post_pk>/comments/<int:pk>/delete/", views.CommentDeleteView.as_view(), name="comment_delete"),
    path("post/<int:pk>/comment/", CommentCreateView.as_view(), name="add-comment"),

    # Tags
    path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts_by_tag"),

    # Search
    path("search/", views.search, name="search"),
]