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
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)


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



class ProductImage(models.Model):

    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="images/")


    def __str__(self):
        
        return f"Image for {self.product.title}"
    

class ProductFeedback(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    comment = models.TextField(max_length=500, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        
        return f"{self.user} review for {self.product}"
    

    def get_average_rating(self):
        
        avg_rating = ProductFeedback.objects.filter(product=self.product).aggregate(models.Avg('rating'))['rating__avg']
        
        return round(avg_rating, 2) if avg_rating is not None else 0 




