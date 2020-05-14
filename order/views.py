from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.utils.crypto import get_random_string

from home.models import UserProfile
from order.models import ShopCartForm, ShopCart, OrderForm, Order, OrderProduct
from product.models import Category, Product


def index(request):
    return HttpResponse("Order App")

@login_required(login_url='/login')
def addtocart(request,id):
    url = request.META.get('HTTP_REFERER')
    checkproduct = ShopCart.objects.filter(product_id=id)
    current_user =request.user
    if checkproduct:
        control =1
    else:
        control = 0
    if request.method == 'POST':
        form = ShopCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data =ShopCart.objects.get(product_id=id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = ShopCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()

            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Ürün Başarılı şekilde Sepete eklendi")
            return HttpResponseRedirect(url)





    else :
        if control == 1:
            data = ShopCart.objects.get(product_id=id)
            data.quantity += 1
            data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            return HttpResponseRedirect(url)
        else:
            current_user = request.user
            data = ShopCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
            request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
            messages.success(request, "Ürün Başarılı şekilde Sepete eklendi")
            return HttpResponseRedirect(url)


@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id = current_user)
    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity

    context ={'schopcart':schopcart,
              'category':category,
              'total':total,
              }

    return render(request,'Shopcart_products.html',context)


@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    return HttpResponseRedirect("/shopcart")

@login_required(login_url='/login')
def orderproduct(request):
    category = Category.objects.all()
    current_user = request.user
    schopcart = ShopCart.objects.filter(user_id=current_user)
    total = 0
    for rs in schopcart:
        total += rs.product.price * rs.quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.first_name = form.cleaned_data['first_name']
            data.last_name = form.cleaned_data['last_name']
            data.address = form.cleaned_data['address']
            data.city = form.cleaned_data['city']
            data.phone = form.cleaned_data['phone']
            data.user_id = current_user.id
            data.total = total
            data.ip = request.META.get('REMOTE_ADDR')
            ordercode = get_random_string(5).upper()
            data.code = ordercode
            data.save()

            schopcart = ShopCart.objects.filter(user_id = current_user.id)
            for rs in schopcart:
                detail = OrderProduct()
                detail.order_id =data.id
                detail.product_id =rs.product_id
                detail.user_id = current_user.id
                detail.quantity = rs.quantity
                product = Product.objects.get(id = rs.product_id)
                product.amount = rs.quantity
                product.save()

                detail.price = rs.product.price
                detail.amount = rs.amount
                detail.save()


            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items'] =0
            messages.success(request,"Siparişiniz verildi, Teşekkürler")
            return render(request,'order_Completed.html',{'ordercode':ordercode,'category':category})
        else:
            messages.error(request,form.errors)
            return HttpResponseRedirect("/order/orderproduct")

    form = OrderForm()
    profile = UserProfile.objects.get(user_id = current_user.id)
    context = {'schopcart':schopcart,
               'category':category,
               'total':total,
               'form':form,
               'profile':profile,}
    return render(request,'Order_Form.html',context)
