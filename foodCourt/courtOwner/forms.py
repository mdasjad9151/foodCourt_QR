from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Owner
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    phone_no = forms.CharField(max_length = 20)
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email', 'phone_no', 'password1', 'password2']



class AddFoodCourt(forms.ModelForm):
    class Meta:
        model = Owner
        fields = ['name','location']