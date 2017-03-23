from django.conf.urls import url
from StudentInformationSystem import views

urlpatterns = [ 
	url(r'^$',views.index,name = 'index'),
	url(r'^base$',views.base,name = 'base'),
	url(r'^display$',views.display,name = 'display')
]