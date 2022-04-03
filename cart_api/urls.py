from django.urls import path
from cart_api.views import add_product_to_chart, validate_cart

urlpatterns = [
    path('add_product/', add_product_to_chart),
    # path('shopping_cart/', shopping_cart),
    path('validate_cart/', validate_cart)
]