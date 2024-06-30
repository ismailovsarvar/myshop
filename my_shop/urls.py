from django.urls import path

from my_shop.views import shop_list

urlpatterns = [
    path('', shop_list, name='shop_list'),
]
