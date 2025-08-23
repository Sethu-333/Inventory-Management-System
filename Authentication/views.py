from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import *


def LoginPage(request):

    if request.user.is_authenticated:

        return redirect('/OM/order/')

    context = {
        "error" : ""
    }
 
    if request.method == 'POST':

        print(request.POST)

        user = authenticate(username = request.POST['username'], password = request.POST['password'] )

        print(user)

        if user is not None:
            
            login(request, user)

            if user.role == 0:
                return redirect('/OM/customers/')
        
            elif user.role == 2:
                return redirect('/OM/order/')
    
        
        else:
            context = {
                "error" : "Invalid username or password"
            }
            return render(request, 'login.html', context)

    return render(request, 'login.html', context)
 
def LogoutPage(request):

    logout(request)

    return redirect('/')

def RegisterPage(request):

    context = {
        "error" : ""
    }

    if request.method == 'POST':

        check_user = User.objects.filter(username = request.POST['username'])

        if len(check_user) > 0:

            context = { "error": "Username Already Exist" }

            return render(request, 'register.html', context)
        else:

            new_user = User(first_name = request.POST['first_name'], last_name = request.POST['last_name'],
                            username = request.POST['username'], email = request.POST['email'], age = request.POST['age'], role = request.POST['role'])
            
            new_user.set_password(request.POST['password'])

            new_user.save()

            return redirect('/')

    return render(request, 'register.html', context)