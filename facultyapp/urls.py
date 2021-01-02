from django.urls import path  
from django.contrib.auth import views as auth_views  
from django.conf.urls import url
from facultyapp import views
from django.conf.urls import include, url
urlpatterns = [   
    url(r'^login/$', views.login),   
    url(r'^auth/',views.validation),
    #url(r'^validation/$',views.validation),
    url(r'^upload/$',views.upload),
    url(r'^home/$',views.home),
    url(r'^reminder_set_student/$',views.reminder_set_student),
    url(r'^addreminder_data/$',views.addreminder_data),
    url(r'^upload_notice/$',views.upload_notice),
    url(r'^set_self_reminder/$',views.set_self_reminder),
    url(r'^add_self_reminder_data/$',views.add_self_reminder_data),
    url(r'^show_self_reminder/$',views.show_self_reminder),
    #url(r'^auth/$', views.auth_view),   
    #url(r'^signup/$',views.signup), 
    #url(r'^invalidlogin/',views.invalidlogin),
    
]