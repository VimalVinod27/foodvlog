from django.urls import path
from. import views
app_name='cart'
urlpatterns=[
path('cart/',views.cartt,name='cartt'),
    path('add_cart/<int:prod_id>',views.add_cart,name='add_cart'),
    path('del_item/<int:id>',views.del_item,name='del_item'),
path('min_cart/<int:id>',views.min_cart,name='min_cart')
]