from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
)

from django.contrib.auth import get_user_model


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ["image", "first_name", "last_name", "username", "email"]
