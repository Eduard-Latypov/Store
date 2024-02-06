from django.contrib import admin

from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "description",
        "price",
        "image",
        "quantity",
        "discount",
        "category",
    ]
