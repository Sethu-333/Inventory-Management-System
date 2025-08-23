from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def CustomerList(request):
    data = customer.objects.all()
    context = {
        'customers' : data
    }
    return render(request, 'customers.html',context)

@login_required(login_url='/')
def AddCustomer(request):
    
    context = {
        'Customer_form' : customer_form()
    }
    if request.method == "POST":
        returned_customer = customer_form(request.POST, request.FILES)
        if returned_customer.is_valid():
            returned_customer.save()
            return redirect('/OM/customers/')

    return render(request, 'customer_add.html', context)

@login_required(login_url='/')
def UpdateCustomer(request, id):
    
    selected_customer = customer.objects.get(id = id)

    context = {
        'Customer_form' : customer_form(instance = selected_customer)
    }

    if request.method == 'POST':
        Customer= customer_form(request.POST, request.FILES, instance= selected_customer)
        if Customer.is_valid():
            Customer.save()
            return redirect('/OM/customers/')
    
    return render(request, 'customer_add.html', context)

@login_required(login_url='/')
def DeleteCustomer(request, id):
    
    selected_customer = customer.objects.get(id = id)
    selected_customer.delete()
    
    return redirect("/OM/customers/")

@login_required(login_url='/')
def AddOrders(request):

    context = {
        'order_form' : order_form()
    }
    if request.method == 'POST':
        
        selected_order = products.objects.get(id = request.POST['product_referance'])

        amount = float(selected_order.price) * float(request.POST['quantity'])

        gst_amount = (amount * selected_order.gst) / 100

        bill_amount = amount + gst_amount

        new_order = order(customer_referance_id = request.POST['customer_referance'], product_referance_id = request.POST['product_referance'], order_number = request.POST['order_number'], order_date = request.POST['order_date'], 
                          quantity = request.POST['quantity'], amount = amount, gst_amount = gst_amount, bill_amount = bill_amount)

        new_order.save()

        return redirect('/OM/order/')

    return render(request, 'order_add.html', context)

@login_required(login_url='/')
def Orders(request):
    
    orders_data = order.objects.all()
    products_data = products.objects.all()

    context = {
        "orders" : orders_data,
        "products_data" : products_data
    }

    return render(request, 'order.html', context)

@login_required(login_url='/')
def UpdateOrder(request, id):
    
    neworder = order.objects.get(id = id)

    context = {
        'order_form' : order_form(instance= neworder)
    }
    
    if request.method == 'POST':
        
        selected_order = products.objects.get(id = request.POST['product_referance'])

        amount = float(selected_order.price) * float(request.POST['quantity'])

        gst_amount = (amount * selected_order.gst) / 100

        bill_amount = amount + gst_amount

        order_filter = order.objects.filter(id = id)
    
        order_filter.update(customer_referance_id = request.POST['customer_referance'], 
                        product_referance_id = request.POST['product_referance'], order_number = request.POST['order_number'], order_date = request.POST['order_date'], 
                        quantity = request.POST['quantity'], amount = amount, gst_amount = gst_amount, bill_amount = bill_amount)

        return redirect('/OM/order/')
    
    return render(request, 'order_add.html', context)

@login_required(login_url='')
def DeleteOrder(request, id):
    
    selected_order = order.objects.get(id = id)
    selected_order.delete()

    return redirect('/OM/order/')
        

