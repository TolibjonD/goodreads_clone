from django.shortcuts import render , redirect
from django.views import View
from .forms import RegistrationForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "users/profile.html", {"user": request.user})

class LogOutView(LoginRequiredMixin , View):
    def get(self, request):
        logout(request)
        messages.info(request, "You have successfully logged out ...")
        return redirect("landing_page")

# ? METHODS => 'GET' && 'POST'
# * URL => '/users/register'
class RegistrationView(View):
    def get(self, request):
        user_creation_form = RegistrationForm()
        context = {
            "form": user_creation_form
        }
        return render(request, "users/register.html" , context)
    
    def post(self , request):
        user_creation_form = RegistrationForm(data=request.POST, files=request.FILES)
        if user_creation_form.is_valid():
            user_creation_form.save()
            messages.info(request, "You have successfully registered...")
            return redirect("users:login")
        else:
            context = {
                "form": user_creation_form
            }
            return render(request, "users/register.html" , context)

# ? METHODS => 'GET' && 'POST'
# * URL => '/users/login'
class LoginPageView(View):
    def get(self , request):
        login_form = AuthenticationForm()
        return render(request , "users/login.html" , {"form": login_form})
    
    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request , user)
            messages.success(request, "You have successfully logged in...")
            return redirect("books:books")
        else:
            return render(request , "users/login.html" , {"form": login_form})
        
class ProfileUpdate(LoginRequiredMixin , View):
    def get(self, request):
        update_form = ProfileUpdateForm(instance=request.user)
        context = {
            "form": update_form
        }

        return render(request, "users/profile_update.html", context)
    
    def post(self, request):
        update_form = ProfileUpdateForm(instance=request.user , data=request.POST, files=request.FILES)
        if update_form.is_valid():
            update_form.save()
            return redirect("users:profile")
        else:
            return render(request, "users/profile_update.html", {"form": update_form})