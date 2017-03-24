from django.conf.urls import url
from StudentInformationSystem import views

urlpatterns = [ 
	url(r'^$',views.index,name = 'index'),
	url(r'^base$',views.base,name = 'base'),
	url(r'^acedamicInfo$',views.acedamicInfo,name = 'acedamicInfo'),
	url(r'^additionalInfo$',views.additionalInfo,name = 'additionalInfo'),
	url(r'^display$',views.display,name = 'display')
]
