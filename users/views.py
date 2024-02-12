from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd["username"], password=cd["password"])
            if user and user.is_active:
                auth.login(request, user)
                messages.success(
                    request, message=f"{cd['username']}, Вы успешно вошли в аккаунт"
                )
                return redirect(reverse("main:index"))
    else:
        form = UserLoginForm()
    context = {"title": "Home - Авторизация", "form": form}
    return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            messages.success(
                request,
                message=f"{user.username}, Вы успешно зарегистрировались и вошли в аккаунт",
            )
            return redirect(reverse("main:index"))
    else:
        form = UserRegisterForm()
    context = {"title": "Home - Регистрация", "form": form}
    return render(request, "users/registration.html", context)


@login_required
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(
            instance=request.user, data=request.POST, files=request.FILES
        )
        if form.is_valid():
            form.save()
            return redirect(reverse("user:profile"))
    else:
        form = UserUpdateForm(instance=request.user)
    context = {"title": "Home - Профиль", "form": form}
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("user:login"))
