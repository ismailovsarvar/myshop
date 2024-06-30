from django.shortcuts import render

from my_shop.models import Product, Comment


# Create your views here.

def shop_list(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/home.html', context)


def detail_list(request, product_id: int):
    product = Product.objects.filter(id=product_id)
    related_products = Product.objects.all()
    products_comments = Comment.objects.filter(product=product_id)

    context = {
        'product_detail': product,
        'related_products': related_products,
        'products_comments': products_comments
    }
    return render(request, 'shop/detail.html', context)
