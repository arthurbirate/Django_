from django.shortcuts import render
from users.models import Profile

from wishlistModule.models import Wishlist, WishlistItem


# Create your views here.


# def customer_wishlist(request, customer_id):
#     profile = Profile.objects.get(id=customer_id)
#     wishlist = Wishlist.objects.filter(profile=profile)
#
#     items = Wishlist.objects.filter(whishlist=wishlist).select_related("product")
#
#     return render(request, 'users/customer_wishlist.html', {"whishlist": wishlist, "items": items})


def customer_wishlist(request, customer_id):
    profile = Profile.objects.get(id=customer_id)
    wishlist = Wishlist.objects.filter(customer=profile).first()

    # Get the items if the wishlist exists, otherwise an empty queryset
    items = wishlist.wishlistitem_set.select_related("product")
    return render(
        request,
        "wishlistModule/customer_wishlist.html",
        {"wishlist": wishlist, "items": items}
    )
