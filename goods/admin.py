from django.contrib import admin

from .models import Categories, Products


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


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
    list_editable = ["discount"]
    search_fields = ["name", "description"]
    list_filter = ["discount", "quantity", "category"]
    prepopulated_fields = {"slug": ["name"]}
