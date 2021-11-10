from django import forms
# from .models import CustomUser, Event, Request
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    user_id = forms.ModelChoiceField(queryset=User.objects.all(),required=False)
    
    class Meta:
        model = User
        fields = ['user_id']