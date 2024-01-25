from .views import (
    RegistrationView, 
    LoginPageView, 
    ProfileView, 
    LogOutView,
    ProfileUpdate
)
from django.urls import path


app_name = "users"
urlpatterns = [
    path("register/", RegistrationView.as_view(), name="register"),
    path("login/", LoginPageView.as_view(), name="login"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("profile/update/", ProfileUpdate.as_view(), name="profile_update"),
    path("logout/", LogOutView.as_view(), name="logout")
]
