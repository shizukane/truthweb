from dataclasses import field
from pyexpat import model
from tkinter import Widget
from django import forms
from .models import Profile,Projects,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['Author', 'pub_date', 'author_profile']
        widgets = {
          'project_description': forms.Textarea(attrs={'rows':4, 'cols':10,}),
        }
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }
        
        
class RegisterForm(RegistrationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        self.helper.form_show_labels = True 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
    widgets = {
        'Name': forms.TextInput(attrs={'class':'form-control'}),
        'Body': forms.Textarea(attrs={'class':'form-control'})

    }    


