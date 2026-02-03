# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    # Optional extra fields not in model
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        required=False
    )

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Write your message'}),
        }
