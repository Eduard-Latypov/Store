from django.urls import path
from .views import *

app_name = "goods"

urlpatterns = [
    path("<slug:slug>/", catalog, name="index"),
    path("product/<slug:slug>/", product_detail, name="product_detail"),
]
