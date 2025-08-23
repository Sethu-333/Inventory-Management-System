from django import forms
from .models import *

class customer_form(forms.ModelForm):

    class Meta():
        model = customer
        fields = '__all__'

        widgets = {
            'customer_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'customer_since' : forms.TextInput(attrs={'class' : 'form-control'}),
            'customer_pic' : forms.FileInput(attrs={'class' : 'form-control'}),
        }

class order_form(forms.ModelForm):

    class Meta():
        model = order
        fields = ['customer_referance', 'product_referance', 'order_number', 'order_date', 'quantity']

        widgets = {
            'customer_referance' : forms.Select(attrs={'class' : 'form-control '}),
            'product_referance' : forms.Select(attrs={'class' : 'form-control'}),
            'order_number':forms.NumberInput(attrs={'class' : 'form-control'}),
            'order_date' : forms.DateInput(attrs={'class' : 'form-control dateplaceholder'}),
            'quantity' : forms.NumberInput(attrs={'class' : 'form-control'})
        }