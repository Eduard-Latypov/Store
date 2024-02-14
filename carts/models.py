from django.contrib.auth import get_user_model
from django.db import models

from goods.models import Products

User = get_user_model()


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Пользователь",
        related_name="carts",
    )
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE, verbose_name="Товар", related_name="carts"
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время добавления"
    )

    objects = CartQueryset().as_manager()

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

    def products_price(self):
        return round(self.product.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f"Корзина {self.user.username} | Товар {self.product.name} | Количество {self.quantity}"

        return f"Анонимная корзина | Товар {self.product.name} | Количество {self.quantity}"
