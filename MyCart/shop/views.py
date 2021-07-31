from django.shortcuts import render
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json
from django.http import HttpResponse

# Create your views here.

def index(request):
    products = Product.objects.all()

    catprods = Product.objects.values('category')

    allprods = {}
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        allprods[cat] = prod

    params={'allprods': allprods}
    return render(request, 'shop/index.html', params)


def search(request):
    query = request.GET.get('search')
    products = Product.objects.all()

    catprods = Product.objects.values('category')
    allprods = {}
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchmatch(query, item)]
        if len(prod) != 0:
            allprods[cat] = prod

    params = {'allprods': allprods, 'msg':''}
    if len(allprods) == 0 or len(query)<4:
        params = {'msg':'Please make sure to enter relevant search query'}
    return render(request, 'shop/search.html', params)


def searchmatch(query,item):
    if query in item.desc.lower() or query in item.product_name.lower() or query in item.category.lower():
        return True
    else:
        return False


def contactus(request):
    thank = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()
        thank = True

    return render(request, 'shop/contactus.html', {'thank':thank})

def tracker(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id','')
        email = request.POST.get('email','')
        try:
            order = Order.objects.filter(order_id=order_id,email=email)
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc, 'time':item.timestamp}) 
                    response = json.dumps([updates, order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')

    return render(request, 'shop/tracker.html')

def aboutus(request):
    return render(request, 'shop/aboutus.html')

def demo(request):
    return render(request, 'shop/demo.html')


def productView(request, myid):
    product = Product.objects.filter(id = myid)
    print(product)
    return render(request, 'shop/prodview.html', {'product':product[0]})


def checkout(request):
    if request.method == 'POST':
        item_json = request.POST.get('item_json','')
        name = request.POST.get('name','')
        amount = request.POST.get('amount','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('email','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')

        order = Order(item_json=item_json,name=name,email=email,address=address,city=city,state=state,zip_code=zip_code,phone=phone,amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc = "The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'shop/checkout.html', {'thank':thank, 'id':id})

    return render(request, 'shop/checkout.html')