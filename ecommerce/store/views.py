from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Category, Product
from .forms import ProductForm

def store(request):

    all_products = Product.objects.all()

    context = {"all_products": all_products}

    return render(request, "store/store.html", context=context)



def categories(request):
    
    all_categories = Category.objects.all()

    return {"all_categories": all_categories}



def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)

    return render(request, "store/list-category.html", {"category": category, "products": products})
    
    



def product_info(request, product_slug):
    
    product = get_object_or_404(Product, slug=product_slug)

    context = {"product": product}

    return render(request, "store/product-info.html", context=context)



# - Getting products posted by current user

@login_required
def my_products(request):

    user = request.user

    products = Product.objects.filter(user=user)

    return render(request, "store/my-products.html", {"products": products})



@login_required
def add_product(request):

    if request.method == "POST":

        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():

            product = form.save(commit=False)

            product.user = request.user

            product.save()

            return redirect("my-products")
        
    else:

        form = ProductForm()
        
    return render(request, "store/add-product.html", {"form": form})

