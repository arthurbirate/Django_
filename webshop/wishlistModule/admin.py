from django.contrib import admin

# Register your models here.

from .models import Wishlist
from .models import WishlistItem

admin.site.register(Wishlist)
admin.site.register(WishlistItem)
