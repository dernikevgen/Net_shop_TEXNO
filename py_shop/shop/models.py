from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from decimal import Decimal
from django.conf import settings


def image_folder(instance, filename):
    '''This is func load correct url_name image'''
    filename = instance.slug + '.' + filename.split('.')[1]
    return f'{instance.slug}/{filename}'


class ThemeFront(models.Model):

    title = models.CharField(max_length=120)
    slug = AutoSlugField(populate_from='title')
    image = models.ImageField(upload_to=image_folder)

    def __str__(self):
        return self.title


class Category(models.Model):

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to=image_folder, blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_slug': self.slug})


class Brand(models.Model):

    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name')
    image = models.ImageField(upload_to=image_folder, blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('brand_detail', kwargs={'brand_slug': self.slug})


class Product(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, db_index=True)
    slug = AutoSlugField(populate_from='title', db_index=True)
    image = models.ImageField(upload_to=image_folder, blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    available = models.BooleanField(default=True, verbose_name='В наличии')
    stock = models.PositiveIntegerField(verbose_name='На складе')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    priority = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'product_slug': self.slug})


class Info(models.Model):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=image_folder, blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('info_detail', kwargs={'info_slug': self.slug})


class Asker(models.Model):

    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to=image_folder, blank=True)
    priority = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('asker_detail', kwargs={'asker_slug': self.slug})


class CartItem(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f'Корзина для товара {self.product.title}'


class Cart(models.Model):

    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)

    def add_to_cart_mod(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        new_item, _ = CartItem.objects.get_or_create(product=product, item_total=product.price)
        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart_mod(self, product_slug):
        cart = self
        product = Product.objects.get(slug=product_slug)
        for cart_item in cart.items.all():
            if cart_item.product == product:
                cart.items.remove(cart_item)
                cart.save()

    def count_qty(self, qty, item_id):
        cart = self
        cart_item = CartItem.objects.get(id=int(item_id))
        cart_item.qty = int(qty)
        cart_item.item_total = int(qty) * Decimal(cart_item.product.price)
        cart_item.save()
        value_cart_total = 0.00
        for item in cart.items.all():
            value_cart_total += float(item.item_total)
        cart.cart_total = value_cart_total
        cart.save()


ORDER_STATUS_CHOICES = (
    ("Принят в обработку", "Принят в обработку"),
    ("Выполняется", "Выполняется"),
    ("Оплачен", "Оплачен"),
)


class Order(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(Cart)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=120)
    buying_type = models.CharField(max_length=40, choices=(("Самовывоз", "Самовывоз"),
                                                           ("Доставка", "Доставка")), default="Доставка")
    sail = models.CharField(max_length=40, choices=(("Наличными", "Наличными"),
                                                    ("Картой", "Картой")), default="Наличными")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(blank=True)
    status = models.CharField(max_length=120, choices=ORDER_STATUS_CHOICES, default="Принят в обработку")

    def __str__(self):
        return f"Заказ под номером {str(self.id)}"
