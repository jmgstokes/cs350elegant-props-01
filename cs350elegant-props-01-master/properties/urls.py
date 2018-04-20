# properties/urls.py

from django.conf.urls import url

from . import views

app_name = 'properties'

urlpatterns = [
    url(r'^$', views.PropertyListView.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.PropertyDetailView.as_view(), name='detail'),
]