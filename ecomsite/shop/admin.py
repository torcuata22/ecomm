from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "ABC Shopping"

#to display more infomration in the admin panel:
class ProductAdmin(admin.ModelAdmin):
    def changeCategoryToDefault(self,request, queryset):
        queryset.update(category='default')

    changeCategoryToDefault.short_description='Default Category'
    list_display=['title', 'price', 'discount_price', 'category']
    search_fields=['title', 'category']
    actions=['changeCategoryToDefault',]
    #fields = ['title', 'price',] this is how you cna hide certain fields
    list_editable=['price', 'category'] #these fields are now editable in the list view

class OrderAdmin(admin.ModelAdmin):
    list_display=["address", "name", "total"]
    search_fields=["address", "name", "total"]

admin.site.register(Products, ProductAdmin)
admin.site.register(Order, OrderAdmin)