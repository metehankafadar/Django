from pyexpat.errors import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


# Create your views here.
from home.forms import SearchForm
from home.models import Setting, ContactFormu, ContactFormMessage
from product.models import Product, Category, Images, Comment


def index(request):
    setting= Setting.objects.get(pk=1)
    sliderdata = Product.objects.all()[:4]
    category=Category.objects.all()
    dayproducts=Product.objects.all()[:4]
    lastproducts = Product.objects.all().order_by('-id')[:3]
    randomproducts = Product.objects.all().order_by('?')[:8]

    context = {'setting': setting,
               'category':category,
               'page':'home',
               'sliderdata':sliderdata,
               'dayproducts':dayproducts,
               'lastproducts':lastproducts,
               'randomproducts':randomproducts}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting= Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting= Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslarimiz.html', context)

def iletisim(request):
    if request.method=='POST':
        form =ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.save()
            messages.success(request,"Mesajınız  başarı ile gönderilmiştir , Teşekkür ederiz")
            return HttpResponseRedirect('/iletisim')
    setting= Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,'form':form}
    return render(request, 'iletisim.html', context)

def category_products(request,id,slug):
    category = Category.objects.all()
    categorydata=Category.objects.get(pk=id)
    products=Product.objects.filter(category_id=id)
    context={'products':products,
             'category':category,
             'categorydata':categorydata,
             'slug':slug}
    return render(request, 'products.html', context)

def products_detail(request,id,slug):
    category = Category.objects.all()
    product=Product.objects.get(pk=id)
    images=Images.objects.filter(product_id=id)
    comments=Comment.objects.filter(product_id=id,status='True')

    context = {'product': product,
               'category': category,
                'product':product,
                'images':images,
                'comments':comments,
               }

    return render(request, 'product_detail.html', context)

def product_search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            products = Product.objects.filter(title__icontains=query)
            context = {'products': products,
                       'category': category,
                       'query': query,
                       }
            return render(request,'products_search.html', context)

    return HttpResponseRedirect('/')


