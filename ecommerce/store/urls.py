from django.urls import path
from django.conf.urls import static
from django.conf import settings

from . import views

urlpatterns = [

    # Main page
    path("", views.store, name="store"),
    
    # Individual product
    path("product/<slug:product_slug>/", views.product_info, name="product-info"),

    # Individual category
    path("search/<slug:category_slug>/", views.list_category, name="list-category"),

    # Products added by user
    path("store/my-products/", views.my_products, name="my-products"),

    # Adding products by user
    path("store/add-product/", views.add_product, name="add-product"),
]

