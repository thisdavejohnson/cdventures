from django.conf.urls import patterns, url

from compliance import views

urlpatterns = patterns('',
#    url(r'^import/', views.importExcel, name='import'),
#    url(r'^$', views.index, name='index'),    
    url(r'^$', views.importExcel, name='import'),    
)
