from django.contrib import admin
from shop.models import ThemeFront, Category, Brand, Product, Info, Asker, Cart, CartItem, Order


class ProductAdmin(admin.ModelAdmin):

    list_display = ['title', 'brand', 'category', 'created', 'updated', 'available', 'priority']
    list_filter = ['priority', 'brand__name', 'category__name']
    search_fields = ['title', 'brand__name']

    class Meta:

        model = Product


class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'priority']
    list_filter = ['priority']

    class Meta:

        model = Category


class BrandAdmin(admin.ModelAdmin):

    list_display = ['name', 'priority']
    list_filter = ['priority']

    class Meta:

        model = Brand


def mark_paid(modeladmin, request, queryset):
    queryset.update(status='Оплачен')


mark_paid.short_description = 'Статус: оплачено'


class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'total', 'date', 'buying_type', 'status']
    list_filter = ['status', 'buying_type']
    search_fields = ['id']
    actions = [mark_paid]

    class Meta:

        model = Order


admin.site.register(ThemeFront)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Info)
admin.site.register(Asker)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Order, OrderAdmin)

