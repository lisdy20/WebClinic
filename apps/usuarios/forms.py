from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Perfil

class PerfilChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model=Perfil

class PerfilCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model=Perfil