from django import forms
from .models import Login

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.RegexField(regex='\d{10,15}', error_message= ("The number must be between 10-15 digits"))
    class Meta:
        model = Login