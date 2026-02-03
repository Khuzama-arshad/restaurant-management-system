# forms.py
from django import forms
from .models import Signup
from django.contrib.auth.models import User

# class SignupForm(forms.ModelForm):
#     class Meta:
#     model = Signup
#     fields = ['username', 'email', 'message'],
class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup  # ✅ REQUIRED
        fields = ['username','first_name','last_name','email', 'password','message']
    # Optional extra fields not in model
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter username'}),
        required=False
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter first name'}),
        required=False
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter last name'}),
        required=False
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}),
        required=False
    )

    # class Meta:
    #     model = Signup
    #     fields = ['name', 'email', 'message']
    #     widgets = {
    #         'name': forms.TextInput(attrs={'placeholder': 'Enter your name'}),
    #         'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
    #         'message': forms.Textarea(attrs={'placeholder': 'Write your message'}),
    #     }
