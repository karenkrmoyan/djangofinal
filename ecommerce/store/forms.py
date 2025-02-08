from django.forms import ModelForm
from django import forms

from .models import Product


class ProductForm(ModelForm):

    class Meta:

        model = Product
        fields = ["category", "title", "brand", "description", "price", "image"]

        widgets = {
            "brand": forms.TextInput(attrs={"placeholder": "Enter a brand name"}),
            "title": forms.TextInput(attrs={"placeholder": "Enter the product title"}),
            "description": forms.Textarea(attrs={"placeholder": "Enter product details", "rows": 3}),
        }

