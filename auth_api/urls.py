from django.urls import path
from auth_api.views import login

urlpatterns = [
    path('login/', login),
]