from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """Custom admin interface for CustomUser model."""
    
    # Fields to be displayed in the admin list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')
    
    # Fields to be used for searching
    search_fields = ('username', 'email', 'first_name', 'last_name')
    
    # Fields to be used for filtering
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'date_joined')
    
    # Fieldsets for organizing the admin form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )
    
    # Fields to be shown when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo')
        }),
    )


# Register the CustomUser with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)