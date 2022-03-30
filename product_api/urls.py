from django.urls import path
from product_api.views import product_list

urlpatterns = [
    path('product/', product_list),
]