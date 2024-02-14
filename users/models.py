from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users_image/%Y/%m/%d/",
        blank=True,
        null=True,
        verbose_name="Аватарка",
    )
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = "Пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
