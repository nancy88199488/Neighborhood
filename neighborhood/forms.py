from django import forms
from .models import Business,Neighborhood,Profile,Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['Admin', 'pub_date', 'admin_profile']
        widgets = {
          'address': forms.Textarea(attrs={'rows':1, 'cols':10,}),
        }

class NewNeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['Admin', 'pub_date', 'admin_profile']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'photo', 'bio']

            

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        widgets = {
          'bio': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }
        
        
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)
    
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        exclude = ['Author', 'pub_date', 'author_profile', 'neighborhood']
        widgets = {
          'post': forms.Textarea(attrs={'rows':2, 'cols':10,}),
        }