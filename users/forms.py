from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import get_user_model


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]
