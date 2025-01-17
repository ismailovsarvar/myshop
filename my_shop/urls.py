from django.urls import path

from my_shop.views import shop_list, detail_list

urlpatterns = [
    path('home/', shop_list, name='shop_list'),
    path('category/<slug:category_slug>/products/', shop_list, name='products_of_category'),
    path('product/<slug:slug>', detail_list, name='detail_list'),
]
