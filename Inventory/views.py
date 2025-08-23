from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

# def AddProduct(request):

#     context = {
#         'product_form' : Product_Form(),
#     }
#     if request.method == "POST":
#         returned_product = Product_Form(request.POST)
#         if returned_product.is_valid():
#             returned_product.save()   

#     return render(request, 'product_add.html', context)

# def ViewProduct(request):

#     all_product = products.objects.all()
#     context = {
#         "all_products" : all_product
#     }
#     return render(request, 'products.html', context)

# def DeleteProduct(request, id):

#     selected_product = products.objects.get(id = id)
#     selected_product.delete()

#     return redirect('/Inventory/products/')

# def UpdateProduct(request, id):

#     selected_product = products.objects.get(id = id)
    
#     context = {
#         'product_form' : Product_Form(instance= selected_product)
#     }

#     if request.method == 'POST':
#         product_form = Product_Form(request.POST, instance= selected_product)
#         if product_form.is_valid():
#             product_form.save()
#             return redirect('/Inventory/products/')
    
#     return render(request, 'product_add.html', context)

class ProductAddView(LoginRequiredMixin , View):

    login_url= '/'
    
    def get(self, request):
        
        context = {
            'product_form' : Product_Form()
        }

        return render(request, 'product_add.html', context)
    
    def post(self, request):
        
        new_product = Product_Form(request.POST, request.FILES)
        if new_product.is_valid():
            new_product.save()

            return redirect('/Inventory/products/')

class ProductListView(LoginRequiredMixin, View):

    login_url= '/'

    def get(self, request):

        all_products = products.objects.all()

        context = {
            'all_products' : all_products
        }

        return render(request, 'products.html', context)

class ProductDeleteView(LoginRequiredMixin, View):

    login_url= '/'

    def get(self, request, id):

        selected_product = products.objects.get(id = id)

        selected_product.delete()

        return redirect('/Inventory/products/')

class ProductUpdateView(LoginRequiredMixin, View):

    login_url= '/'

    def get(self, request, id):
        selected_product = products.objects.get(id = id)

        context = {
            'product_form' : Product_Form(instance= selected_product)
        }

        return render(request, 'product_add.html', context)
    
    def post(self, request, id):

        selected_product = products.objects.get(id = id)

        product_form = Product_Form(request.POST,request.FILES, instance= selected_product)

        if product_form.is_valid():

            product_form.save()

            return redirect('/Inventory/products/')