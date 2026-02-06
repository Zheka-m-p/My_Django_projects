from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    categories_list = models.CategoryModel.objects.all()
    context = {
        'categories_list': categories_list,
    }

    return render(request, 'blog/index.html', context)


def category_page(request, pk, slug):
    category = models.CategoryModel.objects.get(pk=pk)
    context = {
        'category': category,
    }

    return render(request, 'blog/category_page.html', context)

