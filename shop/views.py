from email.policy import default
from logging import exception
from django.shortcuts import render
from django.http import HttpResponse

from shop.models import OrderUpdate
# Create your views here.
def index(request):
    from .models import Product
    from math import ceil
    #products=Product.objects.all()
    #n=len(products)
    #nSlides=ceil(n/4)
    #params={'number_of_slides':nSlides,'product':products,'range':range(1,nSlides)}
    #all_prods=[[nSlides,range(1,nSlides),products],[nSlides,range(1,nSlides),products]]
    #params={'all_prod':all_prods}
    all_prods=[]
    cat_prods=Product.objects.values('category','id')
    cats={item['category'] for item in cat_prods}
    for cat in cats:
        products=Product.objects.filter(category=cat)
        n=len(products)
        nSlides=ceil(n/4)
        all_prods.append([nSlides,range(1,nSlides),products])
    params={'all_prod':all_prods}
    return render(request,'shop/index.html',params)

def searchMatch(query,item):
    if(query in item.product_name.lower() or query in item.category.lower() or query in item.description.lower()):
        return True
    else:
        return False

def search(request):
    from .models import Product
    from math import ceil
    query=request.GET.get('search')
    all_prods=[]
    cat_prods=Product.objects.values('category','id')
    cats={item['category'] for item in cat_prods}
    for cat in cats:
        products=Product.objects.filter(category=cat)
        prod=[item for  item in products if searchMatch(query,item)]
        n=len(prod)
        nSlides=ceil(n/4)
        if n>0:
            all_prods.append([nSlides,range(1,nSlides),prod])
    if len(all_prods)!=0:
        params={'all_prod':all_prods, 'msg':"These are best relevant searches"}
    else:
        params={'all_prod':all_prods, 'msg':"Sorry! could not find relevant searches"}
    return render(request,'shop/search.html',params)

def contact(request):
    from .models import Complain
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        description=request.POST.get('text')
        complain=Complain(name=name, email=email, mobile=mobile, description=description)
        print(name)
        complain.save()
    return render(request,'shop/contact.html')

def about(request):
    return render(request,'shop/about.html')

def productView(request, myid):
    from .models import Product
    product=Product.objects.filter(id=myid)
    params={'product':product[0]}
    return render(request,'shop/productView.html',params)

def tracker(request):
    if(request.method=="POST"):
        from .models import Order
        import json
        order_id=request.POST.get('orderId',"")
        email=request.POST.get('email',"")
        try:
            order=Order.objects.filter(order_id=order_id,email=email)
            if(len(order)>0):
                #name=order.order_id
                update=OrderUpdate.objects.filter(order_id=order_id)
                #print(update.update_desc)
                #return HttpResponse(update)
                #print(update[0].update_desc)
                updates=[]
                n=len(update)
                for i in range(n):
                    updates.append(update[i].update_desc)
                param={'update':update,'i':range(n)}
                return render(request,'shop/tracker.html',param)
            else:
                return HttpResponse("Sorry. We could not find your order")
        except Exception as e:
            return HttpResponse({e})


    return render(request,'shop/tracker.html',{'i':range(0)})

def checkout(request):
    from .models import Order,OrderUpdate
    global thank
    thank=False
    if(request.method=='POST'):
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        phone=request.POST.get('phone')
        amount=request.POST.get('amount')
        order=Order(name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        order_id=order.order_id
        update=OrderUpdate(order_id=order_id,update_desc="Order has been placed")
        update.save()
        thank=True
        global id
        id=order.order_id
    return render(request,'shop/checkout.html',{'thank':thank, 'id':id})