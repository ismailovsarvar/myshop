from django.urls import path

from my_shop.views import shop_list, detail_list

urlpatterns = [
    path('home/', shop_list, name='shop_list'),
    path('detail/<int:product_id>/', detail_list, name='detail_list'),
]
