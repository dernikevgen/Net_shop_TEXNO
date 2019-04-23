from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^remove/(?P<product_id>\d+)/$', views.CartDetail, name='CartRemove'),
    url(r'^add/(?P<product_id>\d+)/$', views.CartDetail, name='CartAdd'),
    url(r'^$', views.CartDetail, name='CartDetail'),
]