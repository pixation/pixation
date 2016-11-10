from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)
# Create your views here.

from accounts.forms import (
    UserLoginForm,
    UserRegisterForm,
)

def login_view(request):
    title = "Login"
    login_form = UserLoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        # To Do: Redirect
        print(request.user.is_authenticated())
    
    return render(request, "form.html", {"form":login_form,"title":title})

def register_view(request):
    title = "Register"
    register_form = UserRegisterForm(request.POST or None)

    return render(request, "form.html", {"form":register_form,"title":title})

def logout_view(request):
    logout(request)
    # To Do: Redirect
    return render(request, "form.html", {})
    