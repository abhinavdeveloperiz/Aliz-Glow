from django.db import models

# Create your models here.


class Products(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True)
    image = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    image4 = models.ImageField(upload_to='products/', null=True, blank=True)
    image5 = models.ImageField(upload_to='products/', null=True, blank=True)
    image6 = models.ImageField(upload_to='products/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"




class Gallery(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"
    


class HomeBanner(models.Model):

    image1 = models.ImageField(upload_to='banner/')
    image2 = models.ImageField(upload_to='banner/')

    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"


class Gif_Section(models.Model):

    gif_image = models.ImageField(upload_to='gifs/')
    title = models.CharField(max_length=100)

    
    class Meta:
        verbose_name = "Gif Section"
        verbose_name_plural = "Gif Sections"




class AboutImage(models.Model):

    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name = "About Image"
        verbose_name_plural = "About Images"
