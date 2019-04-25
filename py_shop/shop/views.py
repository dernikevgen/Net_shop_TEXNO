from django.shortcuts import render
from django.urls import reverse
from shop.models import ThemeFront, Product, Category, Info, Asker, Brand, Cart, CartItem
from django.http import HttpResponseRedirect


def base_view(request):
    '''базовая страница'''
    categories = Category.objects.all()
    products = Product.objects.all()
    images = ThemeFront.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'categories': categories,
        'products': products,
        'images': images,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'cart': cart,
    }
    return render(request, 'base.html', context=context)


def product_view(request, product_slug):
    '''страница товара'''
    product = Product.objects.get(slug=product_slug)
    categories = Category.objects.all()
    products = Product.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'products': products,
        'product': product,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'product.html', context=context)


def category_view(request, category_slug):
    '''страница определённой категории'''
    category = Category.objects.get(slug=category_slug)
    product_of_category = Product.objects.filter(category=category)
    products = Product.objects.all()
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'product_of_category': product_of_category,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'categories': categories,
        'products': products,
        'cart': cart,
    }
    return render(request, 'category.html', context=context)


def category_all_view(request):
    '''страница всех категорий'''
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    cart = Cart.objects.get()
    context = {
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'categories': categories,
        'cart': cart,
    }
    return render(request, 'category_ever.html', context=context)


def brand_view(request):
    '''страница товаров определённого бренда'''
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    cart = Cart.objects.get()
    context = {
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'cart': cart,
    }
    return render(request, 'brands.html', context=context)


def brand_one_view(request, brand_slug):
    '''страница всех брендов'''
    brand = Brand.objects.get(slug=brand_slug)
    product_of_brand = Product.objects.filter(brand=brand)
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    context = {
        'product_of_brand': product_of_brand,
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'cart': cart,
    }
    return render(request, 'brand_one.html', context=context)


def repairs_view(request):
    '''информация(сервис)'''
    categories = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.all()
    cart = Cart.objects.get()
    context = {
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'cart': cart,
    }
    return render(request, 'repairs.html', context=context)


def asker_view_one(request):
    '''информация (вопросы(1))'''
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    cart = Cart.objects.get()
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
        'cart': cart,
    }
    return render(request, 'asker_1.html', context=context)


def asker_view_two(request):
    '''информация (вопросы(2))'''
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    cart = Cart.objects.get()
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
        'cart': cart,
    }
    return render(request, 'asker_2.html', context=context)


def target_view(request):
    '''информация (о портале)'''
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    cart = Cart.objects.get()
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
        'cart': cart,
    }
    return render(request, 'target.html', context=context)


def cart_base_view(request):
    '''страница корзины'''
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    categories = Category.objects.all()
    infos = Info.objects.all()
    brands = Brand.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    context = {
        'cart': cart,
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'cart.html', context=context)


def add_to_cart(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart_mod(product.slug)
    return HttpResponseRedirect(reverse('cart'))


def remove_from_cart(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart_id
        cart = Cart.objects.get(id=cart_id)
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart_mod(product.slug)
    return HttpResponseRedirect(reverse('cart'))












