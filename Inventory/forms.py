from django import forms
from .models import *

class Product_Form(forms.ModelForm):

    class Meta():
        model = products
        fields = '__all__' 

        widgets = {
            "product_name" : forms.TextInput(attrs = {'class' : "form-control"}),
            "product_code" : forms.TextInput(attrs = {'class' : "form-control"}),
            "price" : forms.TextInput(attrs = {'class' : "form-control"}),
            "gst" : forms.TextInput(attrs = {'class' : "form-control"}),
            "picture" : forms.FileInput(attrs= {'class': "form-control"}),
        }
