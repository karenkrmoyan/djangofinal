from django.forms import ModelForm, modelformset_factory
from django import forms

from .models import Product, ProductImage


class ProductForm(ModelForm):

    class Meta:

        model = Product
        fields = ["category", "title", "brand", "description", "price", "image"]

        widgets = {
            "brand": forms.TextInput(attrs={"placeholder": "Enter a brand name"}),
            "title": forms.TextInput(attrs={"placeholder": "Enter the product title"}),
            "description": forms.Textarea(attrs={"placeholder": "Enter product details", "rows": 3}),
        }



class ProductImageForm(ModelForm):

    class Meta:

        model = ProductImage
        fields = ["image"]


ProductImageFormSet = modelformset_factory(ProductImage, form=ProductImageForm, extra=4)  # Adjust extra as needed
