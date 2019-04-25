from django.contrib import admin
from shop.models import ThemeFront, Category, Brand, Product, Info, Asker, Cart, CartItem


class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'brand', 'category', 'created', 'updated', 'available', 'priority']
    list_filter = ['brand__name', 'category__name']
    search_fields = ['title', 'brand__name']

    class Meta:

        model = Product


admin.site.register(ThemeFront)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Info)
admin.site.register(Asker)
admin.site.register(CartItem)
admin.site.register(Cart)

