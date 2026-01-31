from products.models import Category
from cartModule.models import CartItems


def nav_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}
