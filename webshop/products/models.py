from django.db import models
from django.db.models.signals import post_save, post_delete


# Create your models here.

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True, default='default.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=100, null=True, blank=True)
    label = models.CharField(max_length=100, null=True, blank=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    is_sold_out = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name


def productUpdate(sender, instance, created, **kwargs):
    print("Product Saved")


def deleteProduct(sender, instance, **kwargs):
    print("Product Deleted")


post_delete.connect(deleteProduct, sender=Product)

post_save.connect(productUpdate, sender=Product)
