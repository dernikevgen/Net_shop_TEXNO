from django.shortcuts import render
from shop.models import ThemeFront, Product, Category, Info, Asker, Brand, Cart, CartItem, Order
from django.http import JsonResponse, HttpResponseRedirect
from shop.form import OrderForm, RegistrationForm, LoginForm
from django.urls import reverse
from django.contrib.auth import login, authenticate


def base_view(request):
    '''базовая страница'''
    categories = Category.objects.all()
    products = Product.objects.filter(priority=True)
    images = ThemeFront.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.filter(priority=True)
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
    categories = Category.objects.filter(priority=True)
    products = Product.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.filter(priority=True)
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
    categories = Category.objects.filter(priority=True)
    categories_all = Category.objects.all()
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.filter(priority=True)
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
        'categories_all': categories_all,
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
    brands = Brand.objects.filter(priority=True)
    cart = Cart.objects.first()
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
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.filter(priority=True)
    brands_all = Brand.objects.all()
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'infos': infos,
        'askers': askers,
        'brands': brands,
        'inf_infs': inf_infs,
        'brands_all': brands_all,
        'cart': cart,
    }
    return render(request, 'brands.html', context=context)


def brand_one_view(request, brand_slug):
    '''страница всех брендов'''
    brand = Brand.objects.get(slug=brand_slug)
    product_of_brand = Product.objects.filter(brand=brand)
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.filter(priority=True)
    brands_all = Brand.objects.all()
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
        'brands_all': brands_all,
        'cart': cart,
    }
    return render(request, 'brand_one.html', context=context)


def repairs_view(request):
    '''информация(сервис)'''
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    brands = Brand.objects.filter(priority=True)
    cart = Cart.objects.first()
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
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    cart = Cart.objects.first()
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
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    cart = Cart.objects.first()
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
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
        'cart': cart,
    }
    return render(request, 'target.html', context=context)


def history_orders_view(request):
    '''История заказов'''
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    askers = Asker.objects.filter(priority=True)
    cart = Cart.objects.first()
    order = Order.objects.all()
    context = {
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
        'cart': cart,
        'order': order,
    }
    return render(request, 'history_orders.html', context=context)


def cart_base_view(request):
    '''базовая страница корзины'''
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
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
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


def add_to_cart(request):
    '''добавление товара в корзину'''
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
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.add_to_cart_mod(product.slug)
    value_cart_total = 0.00
    for item in cart.items.all():
        value_cart_total += float(item.item_total)
    cart.cart_total = value_cart_total
    cart.save()
    return JsonResponse(
        {
            'cart_total': cart.items.count(),
            'cart_total_final': cart.cart_total,
        }
    )


def remove_from_cart(request):
    '''удаление товара из корзины'''
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
    product_slug = request.GET.get('product_slug')
    product = Product.objects.get(slug=product_slug)
    cart.remove_from_cart_mod(product.slug)
    value_cart_total = 0.00
    for item in cart.items.all():
        value_cart_total += float(item.item_total)
    cart.cart_total = value_cart_total
    cart.save()
    return JsonResponse(
        {
            'cart_total': cart.items.count(),
            'cart_total_final': cart.cart_total,
        }
    )


def count_item_qty(request):
    '''подсчёт суммы от кол-ва товаров и итоговой суммы корзины'''
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
    qty = request.GET.get('qty')
    item_id = request.GET.get('item_id')
    cart_item = CartItem.objects.get(id=int(item_id))
    cart.count_qty(qty, item_id)
    return JsonResponse(
        {
            'cart_total': cart.items.count(),
            'item_total': cart_item.item_total,
            'cart_total_final': cart.cart_total,
        }
    )


def checkout_view(request):
    '''Страница предварительного заказа'''
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
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
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
    return render(request, 'checkout.html', context=context)


def order_create_view(request):
    '''оформления заказа'''
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
    form = OrderForm(request.POST or None)
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    context = {
        'form': form,
        'cart': cart,
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'order.html', context=context)


def make_order_view(request):
    '''cтраница заказа'''
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
    form = OrderForm(request.POST or None)
    images = ThemeFront.objects.all()
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    context = {
        'cart': cart,
        'images': images,
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    if form.is_valid():
        name = form.cleaned_data['name']
        last_name = form.cleaned_data['last_name']
        phone = form.cleaned_data['phone']
        buying_type = form.cleaned_data['buying_type']
        address_true = form.cleaned_data['address_true']
        sail = form.cleaned_data['sail']
        day_half = form.cleaned_data['day_half']
        comments = form.cleaned_data['comments']
        new_order = Order()
        new_order.user = request.user
        new_order.save()
        new_order.items.add(cart)
        new_order.first_name = name
        new_order.last_name = last_name
        new_order.phone = phone
        new_order.sail = sail
        new_order.day_half = day_half
        new_order.address = address_true
        new_order.buying_type = buying_type
        new_order.comments = comments
        new_order.total = cart.cart_total
        new_order.save()
        del request.session['cart_id']
        del request.session['total']
        return HttpResponseRedirect(reverse('thank_you'))
    return render(request, 'thank_you.html', context=context)


def registration_view(request):
    '''страница регестрации и входа'''
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        new_user.username = username
        new_user.set_password(password)
        new_user.email = email
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.save()
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form,
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'registration.html', context=context)


def login_view(request):
    '''Страница входа'''
    categories = Category.objects.filter(priority=True)
    infos = Info.objects.all()
    brands = Brand.objects.filter(priority=True)
    askers = Asker.objects.filter(priority=True)
    inf_infs = Asker.objects.filter(priority=False)
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        login_user = authenticate(username=username, password=password)
        if login_user:
            login(request, login_user)
            return HttpResponseRedirect(reverse('base'))
    context = {
        'form': form,
        'categories': categories,
        'infos': infos,
        'brands': brands,
        'inf_infs': inf_infs,
        'askers': askers,
    }
    return render(request, 'login.html', context=context)




