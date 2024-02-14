from django.contrib import admin

from carts.admin import CartTabInline
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email"]
    list_display_links = ["username", "email"]
    search_fields = ["username", "email", "last_name"]
    inlines = [CartTabInline]
