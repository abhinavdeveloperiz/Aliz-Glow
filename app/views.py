from django.shortcuts import render
from .models import Products,Gallery,HomeBanner
# Create your views here.

def home(request):
    banner=HomeBanner.objects.order_by("-id").first()
    products = Products.objects.order_by("-id")[:8]
    context = {
        'products': products,
        'banner':banner
        }
    return render(request, 'home.html',context)



def about(request):
    return render(request, 'about.html')



def products(request):
    products = Products.objects.order_by("-id")
    context = {
        'products': products
        }
    return render(request, 'products.html',context)

def Product_details(request,id):
    product=Products.objects.get(id=id)
    context={
        'product':product
        }
    return render(request,'product_details.html',context)


def contact(request):
    return render(request, 'contact.html')



def gallery(request):
    gallery_items = Gallery.objects.order_by("-id")
    context = {
        'gallery': gallery_items
        }
    return render(request, 'gallery.html',context)

