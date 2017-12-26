from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^member/$', views.member, name='member'),
    url(r'^item/new/$', views.item_new, name='item_new'),
    url(r'^item/(?P<name>.*)/edit/$', views.item_edit, name='item_edit'),

]