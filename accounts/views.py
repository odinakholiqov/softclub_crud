from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginView(LoginView):
    # form_class = AuthenticationForm
    # authentication_form = None
    template_name = "accounts/login.html"
    # context_object_name = "user"