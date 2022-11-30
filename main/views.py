from django.shortcuts import render
from products.models import Product


def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')
