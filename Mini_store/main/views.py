from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) # только доступные товары

    category = None
    if category_slug:  # если есть категория для фильтрации, то получаем только ее продукты
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)


    sort = request.GET.get('sort', 'name')  # Получаем параметр sort из URL (например, ?sort=price). Если пусто - сортируем по 'name'
    allowed_sorts = ['name', '-name', 'price', '-price'] # защита от сортировок "дурака"

    if sort in allowed_sorts:
        products = products.order_by(sort)

    return render(request, 'main/product/list.html',
                  {'categories': categories, 'category': category, 'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category,
                                              available=True).exclude(id=product.id)[:4]
    # ↑↑↑ предлагаем просмотреть доп. продукты из этой же категории ↑↑↑
    cart_product_form = CartAddProductForm()

    return render(request, 'main/product/detail.html',
                  context={'product': product,
                           'related_products': related_products,
                           'cart_product_form': cart_product_form})
