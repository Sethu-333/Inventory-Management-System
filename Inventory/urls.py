from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('products/add/', ProductAddView.as_view()),
    path('products/',ProductListView.as_view()),
    path('products/delete/<int:id>/', ProductDeleteView.as_view(), name = 'product_delete'),
    path('products/update/<int:id>/', ProductUpdateView.as_view(), name = 'product_update'),
]

