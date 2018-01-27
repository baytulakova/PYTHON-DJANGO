from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^site1',views.category, name='category'),
    url(r'^site2',views.phones,name='phones'),
    url(r'^site3',views.proc,name='proc'),
    url(r'^site4',views.op,name='op'),
    url(r'^site5',views.usb,name='usb'),
    url(r'^site5',views.usb,name='usb'),
    url(r'^site6',views.zakaz,name='zakaz'),

    # url(r'^(?P<categoryId>[0-9]+)/$', views.category, name='category'),
    # url(r'^(?P<productId>[0-9]+)/products/$', views.product, name='products'),
]
