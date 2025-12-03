from django.shortcuts import render, get_object_or_404
from .models import Products, Gallery, HomeBanner


def home(request):
    banner = HomeBanner.objects.only("image1", "image2").order_by("-id").first()

  
    products = Products.objects.only(
        "id", "name", "price", "image","image2"
    ).order_by("-id")[:8]

    return render(request, "home.html", {
        "products": products,
        "banner": banner,
    })


def about(request):
    return render(request, "about.html")



def products(request):
   
    products = Products.objects.only("id", "name", "price", "image","image2").order_by("-id")

    return render(request, "products.html", {
        "products": products
    })


def Product_details(request, id):
  
    product = get_object_or_404(Products, id=id)

    return render(request, "product_details.html", {
        "product": product
    })


def contact(request):
    return render(request, "contact.html")



def gallery(request):
    gallery_items = Gallery.objects.only("id", "title", "image").order_by("-id")

    return render(request, "gallery.html", {
        "gallery": gallery_items
    })


def privacy_policy(request):
    return render(request, "privacy_policy.html")
