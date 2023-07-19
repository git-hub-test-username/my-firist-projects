from django.shortcuts import render
from django.http import HttpResponse

from myapp.models import Dastavka


def all_product(request):
    products = Dastavka.objects.all().order_by('-id')
    
    
    context = {
        'products': products,
    }

    return render(request,'all_product.html',context)




def completed_product(request):
    products = Dastavka.objects.filter(status='Yetqazib berilgan').order_by('-id')

    context = {
        'products' : products,
    }

    return render (request, "completed_product.html",context )



def waiting_product(request):
    products = Dastavka.objects.filter(status='Tayyorlanmoqda!').order_by('-id')

    context = {
        'products' : products,
    }

    return render (request, "waiting_product.html",context )