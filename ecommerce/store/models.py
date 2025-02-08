from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    
    name = models.CharField(max_length=250, db_index=True)
    slug = models.CharField(max_length=250, unique=True)


    class Meta:
        verbose_name_plural = "categories"


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        
        return reverse("list-category", args=[self.slug])
    

class Product(models.Model):
    
    category = models.ForeignKey(Category, related_name="product", on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default="un-branded")
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to="images/")


    class Meta:
        verbose_name_plural = "products"

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        
        return reverse("product-info", args=[self.slug])
    
    # - Saving the slug field when user is posting a product
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs) 