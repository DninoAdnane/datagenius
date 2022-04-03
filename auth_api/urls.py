from django.urls import path
from auth_api.views import login, signin

urlpatterns = [
    path('login/', login),
    path('signin/', signin)
]