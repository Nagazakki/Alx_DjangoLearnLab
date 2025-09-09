# relationship_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

# Function-based views approach
def user_login(request):
    """
    Handle user login using function-based view
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('home')  # Redirect to home or desired page
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    
    form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    """
    Handle user logout
    """
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return render(request, 'relationship_app/logout.html')

def user_register(request):
    """
    Handle user registration using function-based view
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to home or desired page
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    
    form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Class-based views approach (alternative implementation)
class CustomLoginView(LoginView):
    """
    Custom login view using Django's built-in LoginView
    """
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('home')  # Redirect after successful login
    
    def form_valid(self, form):
        messages.success(self.request, 'You have successfully logged in!')
        return super().form_valid(form)

class CustomLogoutView(LogoutView):
    """
    Custom logout view using Django's built-in LogoutView
    """
    template_name = 'relationship_app/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'You have successfully logged out!')
        return super().dispatch(request, *args, **kwargs)

class CustomRegisterView(CreateView):
    """
    Custom registration view using CreateView
    """
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}!')
        login(self.request, self.object)  # Log in the user after registration
        return response

# Protected view example (requires login)
@login_required
def profile_view(request):
    """
    Example of a protected view that requires authentication
    """
    return render(request, 'relationship_app/profile.html', {'user': request.user})

# Your existing relationship_app views can go here
# For example, if you have existing views for your app:

def home_view(request):
    """
    Home page view
    """
    return render(request, 'relationship_app/home.html')

# Add any other existing views from your relationship_app here