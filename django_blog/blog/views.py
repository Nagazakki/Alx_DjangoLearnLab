from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

@login_required
def profile_view(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, "blog/profile.html", {"user_form": user_form, "profile_form": profile_form})

def home(request):
    return render(request, "blog/home.html")
def post_list(request):
    return render(request, "blog/post_list.html")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, "registration/profile.html", {
        "user_form": user_form,
        "profile_form": profile_form,
    })

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"  # or templates/blog/post_list.html
    context_object_name = "posts"
    ordering = ["-published_date"]
    paginate_by = 10  # optional

# Detail view - accessible to all
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"  # templates/blog/post_detail.html
    context_object_name = "post"

# Create view - only for logged in users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"
    # on success redirect to post detail; CreateView will use get_absolute_url if present
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# Update view - only the author can update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Delete view - only the author can delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("posts")  # redirect to posts list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author