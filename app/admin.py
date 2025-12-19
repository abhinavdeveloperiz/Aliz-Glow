from django.contrib import admin
from django.utils.html import format_html
from .models import Products, Gallery, HomeBanner,Gif_Section, AboutImage

# --- Products Admin ---
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_tag', 'image2_tag', 'image3_tag')
    search_fields = ('name', 'description')
    list_filter = ('price',)
    readonly_fields = ('image_tag', 'image2_tag', 'image3_tag', 'image4_tag', 'image5_tag', 'image6_tag')

    # Function to display images in admin
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image 1'

    def image2_tag(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="80" style="object-fit: cover;" />', obj.image2.url)
        return "-"
    image2_tag.short_description = 'Image 2'

    def image3_tag(self, obj):
        if obj.image3:
            return format_html('<img src="{}" width="80" style="object-fit: cover;" />', obj.image3.url)
        return "-"
    image3_tag.short_description = 'Image 3'

    def image4_tag(self, obj):
        if obj.image4:
            return format_html('<img src="{}" width="80" style="object-fit: cover;" />', obj.image4.url)
        return "-"
    image4_tag.short_description = 'Image 4'

    def image5_tag(self, obj):
        if obj.image5:
            return format_html('<img src="{}" width="80" style="object-fit: cover;" />', obj.image5.url)
        return "-"
    image5_tag.short_description = 'Image 5'

    def image6_tag(self, obj):
        if obj.image6:
            return format_html('<img src="{}" width="80" style="object-fit: cover;" />', obj.image6.url)
        return "-"
    image6_tag.short_description = 'Image 6'

# --- Gallery Admin ---
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ('title',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return "-"
    image_tag.short_description = 'Image'

# --- Banner Admin ---
# --- Banner Admin ---
class HomeBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'image1_tag', 'image2_tag')
    readonly_fields = ('image1_tag', 'image2_tag')
    
    # Display Image 1
    def image1_tag(self, obj):
        if obj.image1:
            return format_html('<img src="{}" width="120" style="object-fit: cover;" />', obj.image1.url)
        return "-"
    image1_tag.short_description = 'Image 1'

    # Display Image 2
    def image2_tag(self, obj):
        if obj.image2:
            return format_html('<img src="{}" width="120" style="object-fit: cover;" />', obj.image2.url)
        return "-"
    image2_tag.short_description = 'Image 2'



# --- Gif Section Admin ---
class GifSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'gif_tag')
    search_fields = ('title',)
    readonly_fields = ('gif_tag',)

    def gif_tag(self, obj):
        if obj.gif_image:
            return format_html(
                '<img src="{}" width="120" style="object-fit: cover;" />',
                obj.gif_image.url
            )
        return "-"
    gif_tag.short_description = 'GIF Preview'




# --- About Image Admin ---
class AboutImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image1_tag', 'image2_tag')
    readonly_fields = ('image1_tag', 'image2_tag')

    def image1_tag(self, obj):
        if obj.image1:
            return format_html(
                '<img src="{}" width="120" style="object-fit: cover;" />',
                obj.image1.url
            )
        return "-"
    image1_tag.short_description = 'Image 1'

    def image2_tag(self, obj):
        if obj.image2:
            return format_html(
                '<img src="{}" width="120" style="object-fit: cover;" />',
                obj.image2.url
            )
        return "-"
    image2_tag.short_description = 'Image 2'



# Registering models with admin
admin.site.register(HomeBanner, HomeBannerAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Gif_Section, GifSectionAdmin)
admin.site.register(AboutImage, AboutImageAdmin)



admin.site.site_header = "AlizGlow Admin"
admin.site.site_title = "AlizGlow Admin Portal"
admin.site.index_title = "Welcome to AlizGlow Admin"
