from django.urls import path
from .views import *

app_name = "goods"

urlpatterns = [
    path("", catalog, name="catalog"),
    path("product/", product, name="product"),
]
