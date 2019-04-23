from django.conf.urls import url
from shop import views
from shop.views import base_view, category_view, category_all_view, brand_view, repairs_view
from shop.views import asker_view_one, asker_view_two, target_view, brand_one_view, product_view

urlpatterns = [
    url(r'^$', views.base_view, name='base'),
    url(r'^category_ever/$', category_all_view, name='category_ever'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    url(r'^brand_ever/$', brand_view, name='brand_ever'),
    url(r'^brand/(?P<brand_slug>[-\w]+)/$', brand_one_view, name='brand_detail'),
    url(r'^repairs/$', repairs_view, name='repairs'),
    url(r'^asker_1/$', asker_view_one, name='asker_1'),
    url(r'^asker_2/$', asker_view_two, name='asker_2'),
    url(r'^target/$', target_view, name='target'),
]

