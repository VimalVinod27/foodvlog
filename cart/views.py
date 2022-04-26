from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from .models import *
from shop.models import *

# Create your views here.
def cartt(request):
    cart=None
    categ=Category.objects.all()

    try:
        cart = Cart_list.objects.get(cart_user_id=cart_id(request))
        cart_itms = Cart_items.objects.filter(cart=cart)
    except:
        cart_itms = Cart_items.objects.filter(cart=cart)

    tot=0

    for i in cart_itms:
        tot+=i.sub_total()




    return render(request,'cart.html',{'item':cart_itms,'total':tot,'categ':categ})

def cart_id(request):
    ct_id=request.session.get('member_id')
    #if not ct_id:
        #ct_id=request.session.create()
        #ct_id=request.session.session_key
    return ct_id

def add_cart(request,prod_id):
    prodt=Product.objects.get(id=prod_id)
    ct_id=cart_id(request)
    try:
        cart = Cart_list.objects.get(cart_user_id=ct_id)
    except:
        cart=Cart_list.objects.create(cart_user_id=ct_id)
    try:
        c_item=Cart_items.objects.get(prodt=prodt,cart=cart)
        if c_item.quant<c_item.prodt.stock:
            c_item.quant += 1
            c_item.save()

    except:
        c_item = Cart_items.objects.create(prodt=prodt, cart=cart, quant=1)

    return redirect('cart:cartt')


def del_item(request,id):
    c_item=Cart_items.objects.get(id=id)
    #cart=Cart_list.objects.get(cart_user_id=cart_id(request))
    #prodt=get_object_or_404(Product,id=prodt_id)
    #c_item=Cart_items.objects.get(prodt=prodt,cart=cart)
    c_item.delete()
    return redirect('cart:cartt')

def min_cart(request,id):
    c_item=Cart_items.objects.get(id=id)
    #cart=Cart_list.objects.get(cart_user_id=cart_id(request))
    #prodt=get_object_or_404(Product,id=prodt_id)
    #c_item=Cart_items.objects.get(prodt=prodt,cart=cart)

    if c_item.quant>1:
        c_item.quant-=1
        c_item.save()
    else:
        c_item.delete()
    return redirect('cart:cartt')











