from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request, 'Homepage.html')
   #return HttpResponse("this is homepage")

def payment(request):
    return render(request, 'payment.html')

def regstray(request):
    return render(request, 'regstray.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')


def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store.html', context)


def regstray(request):
    if request.method == "POST":
        name = request.POST.get('name')
        pname = request.POST.get('pname')
        img = request.POST.get('img')
        local = request.POST.get('local')
        desc = request.POST.get('desc')
        regstray = Regstray(name=name, pname=pname, img=img, local=local, desc=desc, ) 

        regstray.save()
        messages.success(request, 'Your form has been submitted!')

   
    return render(request, 'regstray.html')

def about(request):
    return render(request, 'about.html')


def goods(request):
     if request.method == "POST":
        name = request.POST.get('name')
        date = request.POST.get('date')
        email = request.POST.get('email')
        number = request.POST.get('number')
        local = request.POST.get('local')
        goods = Goods(name=name, date=date, email=email, number=number, local=local, ) 

        goods.save()


     return render(request, 'goods.html')
