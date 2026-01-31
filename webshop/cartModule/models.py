from django.db import models

from products.models import Product


# Create your models here.

class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart number: {self.id}"


class CartItems(models.Model):
    id = models.AutoField(primary_key=True)
    Cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return f"Item number: {self.id}"

    @property
    def total_price(self):
        return self.quantity * self.product.price
