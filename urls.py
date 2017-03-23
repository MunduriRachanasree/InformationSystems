from django.conf.urls import url
from .import views

urlpatterns = [
		
		url(r'^index/$',views.index,name='index'),
		url(r'^success/$',views.success,name='success'),
		url(r'^display/$',views.display,name='display'),
		
]