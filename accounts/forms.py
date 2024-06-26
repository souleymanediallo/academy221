from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse Email",
            "password1": "Mot de passe",
            "password2": "Confirmer le mot de passe",
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})



class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']
        labels = {
            "first_name": "Prénom",
            "last_name": "Nom",
            "email": "Adresse Email",
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'description']
        labels = {
            "image": "Photo de profil",
            "description": "Description de votre profile",
        }

    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

        self.fields['image'].widget.attrs.update({
            'class': 'form-control-file'
        })