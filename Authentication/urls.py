from django.urls import path
from .views import *

urlpatterns = [
    path('', LoginPage),
    path('logout/', LogoutPage),
    path('register/', RegisterPage),
]