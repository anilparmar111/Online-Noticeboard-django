from django.urls import path  
from django.contrib.auth import views as auth_views  
from django.conf.urls import url
from adminloginapp import views
from django.conf.urls import include, url
urlpatterns = [   
    url(r'^login/$', views.login),   
    url(r'^auth/$', views.auth_view),   
    url(r'^signup/$',views.signup), 
    url(r'^invalidlogin/',views.invalidlogin),
    url(r'^insert/',views.insert),   
    url(r'^logout/',views.logout), 
    #url(r'^insertfaculty/',views.insertfaculty),
]