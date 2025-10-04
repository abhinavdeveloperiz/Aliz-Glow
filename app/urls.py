from django.urls import path, include
from app import views


urlpatterns = [

    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('products/',views.products, name='products'),
    path('contact/',views.contact, name='contact'),
    path('gallery/',views.gallery, name='gallery'),
    path('product/<int:id>/',views.Product_details, name='product_details'),

]