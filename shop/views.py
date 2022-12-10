from django.db.models import Q
from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.
def shopindex(request,categ_slug=None,search=None):

    categ_items=None
    categ=Category.objects.all()
    if categ_slug!=None:
        categ_items= Product.objects.filter(category__slug=categ_slug,available=True)
    else:
        key = request.GET.get('srch')
        if key is not None:
            categ_items = Product.objects.filter(Q(name__icontains=key) | Q(desc__icontains=key),available=True)
            if not categ_items:
                return render(request, 'nomatch.html')


        else:
            categ_items = Product.objects.filter(available=True)


    paginator = Paginator(categ_items, 4)
    try:
        if request.GET.get('page'):
            page = int(request.GET.get('page'))
            page_obj = paginator.page(page)
        else:
            page_obj = paginator.page(1)
    except (EmptyPage,InvalidPage):
        page=paginator.num_pages
        page_obj = paginator.page(page)



    return render(request,'index.html',{'fd_items':categ_items,'categ':categ,'page_obj':page_obj})

def shop_detail(request,categ_slug,prod_slug):
    categ=Category.objects.all()#to get category dropdown in detail page
    prodt=Product.objects.get(slug=prod_slug,category__slug=categ_slug)
    stk=True
    if prodt.stock<1:
        stk=False

    return render(request,'product_detail.html',{'prodt':prodt,'categ':categ,'stk':stk})

#def search(request):
 #   key=request.GET.get('srch')
  #  if key is not None:
   #     obj = Product.objects.filter(Q(name__icontains=key) | Q(desc__icontains=key))
    #    print(key)
     #   return redirect(shopindex, kwargs={'search': obj})
    #else:
     #   return render(request,'nomatch.html')




