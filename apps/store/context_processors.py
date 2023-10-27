from .models import Category

def menu_categories(requset):
    categories = Category.objects.all()

    return {'menu_categores': categories}