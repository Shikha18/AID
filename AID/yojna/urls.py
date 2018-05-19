from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^$',views.home,name='home'),
	url(r'^(?P<id>\d+)/$',views.field,name='field'),
	url(r'^(?P<id>\d+)/(?P<range>\d+)$',views.field,name='field'),
	url(r'^ajax/$',views.ajax,name='ajax')

]