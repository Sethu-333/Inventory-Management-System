from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('customers/',CustomerList),
    path('customers/add/', AddCustomer),
    path('customers/update/<int:id>/', UpdateCustomer, name = 'update_customer'),
    path('customers/delete/<int:id>/', DeleteCustomer, name = 'delete_customer'),
    path('order/', Orders),
    path('order/add/',AddOrders),
    path('order/update/<int:id>/', UpdateOrder, name= "order_update"),
    path('order/delete/<int:id>/', DeleteOrder, name= "order_delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)