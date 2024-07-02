from django.shortcuts import render

from my_shop.models import Product, Comment, Category


# Create your views here.

def shop_list(request, category_slug=None):
    categories = Category.objects.all()
    products = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def detail_list(request, product_id, slug):
    product = Product.objects.filter(id=product_id)
    related_products = Product.objects.get(slug=slug)
    products_comments = Comment.objects.filter(product=product_id)

    context = {
        'product_detail': product,
        'related_products': related_products,
        'products_comments': products_comments
    }
    return render(request, 'shop/detail.html', context)
