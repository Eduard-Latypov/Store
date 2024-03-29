from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.db.models import Prefetch
from django.shortcuts import render, redirect
from django.urls import reverse

from carts.models import Cart
from orders.models import Order, OrderItem
from .forms import UserLoginForm, UserRegisterForm, UserUpdateForm


class UserLoginView(LoginView):
    """Хотел все вьюхи сделать функциями, но тут получается
    избыточно кода и причем не красиво, поэтому сделал CBV"""

    template_name = "users/login.html"
    form_class = UserLoginForm

    def form_valid(self, form):
        session_key = self.request.session.session_key
        self._set_carts_from_session_to_user(form)
        response = super().form_valid(form)
        messages.success(
            self.request, f"{self.request.user.username}, Вы успешно вошли в аккаунт"
        )

        return response

    def _set_carts_from_session_to_user(self, form):
        session_key = self.request.session.session_key
        if session_key:
            user = form.get_user()
            carts = Cart.objects.filter(session_key=session_key)
            if carts.exists():
                carts.update(user=user)


# def login(request):
#     if request.method == "POST":
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = auth.authenticate(username=cd["username"], password=cd["password"])
#             if user and user.is_active:
#                 auth.login(request, user)
#                 messages.success(
#                     request, message=f"{cd['username']}, Вы успешно вошли в аккаунт"
#                 )
#                 if request.POST.get("next", None):
#                     return redirect(request.POST.get("next"))
#                 return redirect(reverse("main:index"))
#     else:
#         form = UserLoginForm()
#     context = {"title": "Home - Авторизация", "form": form}
#     return render(request, "users/login.html", context)


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            session_key = request.session.session_key
            auth.login(request, user)

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)
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
    orders = (
        Order.objects.filter(user=request.user)
        .prefetch_related(
            Prefetch(
                "orderitem_set",
                queryset=OrderItem.objects.select_related("product"),
            )
        )
        .order_by("-id")
    )

    context = {
        "title": "Home - Кабинет",
        "form": form,
        "orders": orders,
    }
    return render(request, "users/profile.html", context)


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse("user:login"))


def users_cart(request):
    return render(request, "users/users_cart.html")
