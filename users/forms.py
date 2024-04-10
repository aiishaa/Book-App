
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class UserModelForm(forms.ModelForm):
    class Meta:
        model  = User
        fields= ('first_name', 'last_name', 'email', 'username', 'password')


    def save(self, commit=True):
        self.instance.password= make_password(password=self.instance.password)
        super().save()
        return self.instance
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')