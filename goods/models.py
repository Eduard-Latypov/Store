from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Слаг")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название товара")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Слаг")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="%Y/%m/%d/", blank=True, null=True, verbose_name="Изображение"
    )
    price = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.00, verbose_name="Цена"
    )
    discount = models.PositiveIntegerField(default=0, verbose_name="Скидка в %")
    quantity = models.PositiveIntegerField(default=0, verbose_name="Количество")
    category = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категория",
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
