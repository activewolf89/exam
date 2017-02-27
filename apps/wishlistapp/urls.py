from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name = "my_index"),
    url(r'^create', views.create, name = "create"),
    url(r'^this_product', views.this_product, name = "this_product"),
    url(r'^(?P<id>\d+)$', views.show, name = "show"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name = "remove"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = "delete"),
    url(r'^add/(?P<id>\d+)$', views.add, name = "add")
]
