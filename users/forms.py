from django import forms
from users.models import CustomUser
from django.core.mail import send_mail


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = CustomUser
        fields = ("username", "first_name" , "last_name", "email" , "password", "profile_picture")

    def save(self, commit = True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user
    
       
    

    

class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email", "profile_picture")
