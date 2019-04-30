from django.conf.urls import url
from shop import views
from django.conf import settings
from django.contrib.auth.views import LogoutView
from shop.views import base_view, category_view, category_all_view, brand_view, repairs_view
from shop.views import asker_view_one, asker_view_two, target_view, brand_one_view, product_view
from shop.views import cart_base_view, add_to_cart, remove_from_cart, count_item_qty, checkout_view
from shop.views import order_create_view, make_order_view, history_orders_view

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
    url(r'^add_to_cart/$', add_to_cart, name='add_to_cart'),
    url(r'^remove_from_cart/$', remove_from_cart, name='remove_from_cart'),
    url(r'^count_item_qty/$', count_item_qty, name='count_item_qty'),
    url(r'^cart/$', cart_base_view, name='cart'),
    url(r'^checkout/$', checkout_view, name='checkout'),
    url(r'^order/$', order_create_view, name='order'),
    url(r'^thank_you/$', make_order_view, name='thank_you'),
    url(r'^history_orders/$', history_orders_view, name='history_orders'),
    url(r'^logout/$', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
