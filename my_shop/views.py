from django.shortcuts import render

from my_shop.models import Product, Comment, Category


# Create your views here.

def shop_list(request, category_slug=None):
    categories = Category.objects.all()
    search_query = request.GET.get('search')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query)
    else:
        products = Product.objects.all()
    if category_slug:
        products = products.filter(category__slug=category_slug)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def detail_list(request, slug, product_id: int):
    product = Product.objects.get(slug=slug)
    related_products = Product.objects.all()
    products_comments = Comment.objects.filter(product=product_id)

    context = {
        'product': product,
        'related_products': related_products,
        'products_comments': products_comments
    }
    return render(request, 'shop/detail.html', context)
