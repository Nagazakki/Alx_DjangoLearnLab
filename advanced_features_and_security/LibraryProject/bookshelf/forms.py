from django import forms
from .models import Book


class ExampleForm(forms.Form):
    """
    Example form for demonstration purposes
    """
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class BookForm(forms.ModelForm):
    """
    Form for creating and editing books with built-in validation
    """
    class Meta:
        model = Book
        fields = ['title', 'author']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter book title',
                'maxlength': 200
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Enter author name',
                'maxlength': 100
            })
        }

    def clean_title(self):
        """Custom validation for title field"""
        title = self.cleaned_data.get('title')
        if not title or not title.strip():
            raise forms.ValidationError('Title cannot be empty')
        return title.strip()

    def clean_author(self):
        """Custom validation for author field"""  
        author = self.cleaned_data.get('author')
        if not author or not author.strip():
            raise forms.ValidationError('Author cannot be empty')
        return author.strip()