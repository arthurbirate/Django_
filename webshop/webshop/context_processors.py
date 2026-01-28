from products.models import Category


def nav_categories(request):
    categories = Category.objects.all()
    return {"categories": categories}
