from django.shortcuts import render, get_object_or_404, render_to_response
from shop.models import ThemeFront, Product, Category, Info, Asker, Brand
from cart.cart import

def base_view(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    images = ThemeFront.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'categories': categories,
        'products': products,
        'images': images,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
    }
    return render(request, 'base.html', context=context)


def product_view(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    products = Product.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'products': products,
        'product': product,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'categories': categories,
    }
    return render(request, 'product.html', context=context)


def category_view(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    product_of_category = Product.objects.filter(category=category)
    products = Product.objects.all()
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'product_of_category': product_of_category,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'categories': categories,
        'products': products,
    }
    return render(request, 'category.html', context=context)


def category_all_view(request):
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'categories': categories,
    }
    return render(request, 'category_ever.html', context=context)


def brand_view(request):
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
    }
    return render(request, 'brands.html', context=context)


def brand_one_view(request, brand_slug):
    brand = Brand.objects.get(slug=brand_slug)
    product_of_brand = Product.objects.filter(brand=brand)
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'product_of_brand': product_of_brand,
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
    }
    return render(request, 'brand_one.html', context=context)


def repairs_view(request):
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    context = {
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
    }
    return render(request, 'repairs.html', context=context)


def asker_view_one(request):
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'asker_1.html', context=context)


def asker_view_two(request):
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'asker_2.html', context=context)


def target_view(request):
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'target.html', context=context)







