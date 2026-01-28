from django.contrib.auth.models import User
from django.db import models
from products.models import Product

from users.models import Profile


# Create your models here.

class Wishlist(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name}'wishlist"


class WishlistItem(models.Model):
    id = models.AutoField(primary_key=True)
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="items")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product} in {self.wishlist}"
