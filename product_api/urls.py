from django.urls import path
from product_api.views import product_list, product_select, product_rayon, product_prix

urlpatterns = [
    path('product/', product_list),
    path('product_select/<str:name>/', product_select),
    path('product_rayon/<str:rayon>/', product_rayon),
    path('product_prix', product_prix)
]