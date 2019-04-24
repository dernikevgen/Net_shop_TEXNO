from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse
from decimal import Decimal


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








