from cart.views import *
from cart.models import *



def count(request):

    itc = 0
    if 'admin' in request.path:
        return {}
    try:
        cart = Cart_list.objects.get(cart_user_id=cart_id(request))
        c_itms = Cart_items.objects.filter(cart=cart)
        for i in c_itms:
            itc += i.quant
    except Cart_list.DoesNotExist:
        itc = 0
    return dict(item_count=itc)
