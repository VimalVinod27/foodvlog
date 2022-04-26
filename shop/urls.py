from django.urls import path
from. import views

app_name='shop'
urlpatterns=[
    path('',views.shopindex,name='shopindex'),
    path('<slug:categ_slug>',views.shopindex,name='shop_category'),
    path('<slug:categ_slug>/<slug:prod_slug>',views.shop_detail,name='shop_detail'),
    #path('cart/',views.cartt,name='cartt')
]