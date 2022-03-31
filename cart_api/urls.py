from django.urls import path
from cart_api.views import add_product_to_chart

urlpatterns = [
    path('add_product/', add_product_to_chart)
]