from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Category, Product, ProductImage, ProductFeedback
from .forms import ProductForm, ProductImageFormSet

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
    
    


@login_required
def product_info(request, product_slug):
    
    product = get_object_or_404(Product, slug=product_slug)

    feedbacks = ProductFeedback.objects.filter(product=product)

    avg_rating = ProductFeedback.get_average_rating

    if request.method == "POST":
        rating = int(request.POST.get('rating', 0))
        comment = request.POST.get('comment', '').strip()

        ProductFeedback.objects.create(
            product=product,
            user=request.user,
            rating=rating,
            comment=comment
        )
        
        return redirect('product-info', product_slug=product.slug)

    context = {
        "product": product,
        "feedbacks": feedbacks,
        "avg_rating": avg_rating,
    }

    return render(request, "store/product-info.html", context)



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

        formset = ProductImageFormSet(request.POST, request.FILES, queryset=ProductImage.objects.none())

        if form.is_valid() and formset.is_valid():

            product = form.save(commit=False)

            product.user = request.user

            product.save()


            for image_form in formset:

                if image_form.cleaned_data.get("image"):
                    
                    ProductImage.objects.create(product=product, image=image_form.cleaned_data['image'])


            return redirect("my-products")
        
    else:

        form = ProductForm()

        formset = ProductImageFormSet(queryset=ProductImage.objects.none())
        
    return render(request, "store/add-product.html", {"form": form, "formset": formset})

