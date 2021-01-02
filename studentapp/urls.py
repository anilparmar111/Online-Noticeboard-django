from django.urls import path  
from django.contrib.auth import views as auth_views  
from django.conf.urls import url
from studentapp import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
urlpatterns = [   
    url(r'^login/$',views.login),
    url(r'^course/$', views.course),  
    url(r'^auth/$',views.auth), 
    url(r'^home/$',views.home),
    url(r'^set_reminder/$',views.set_reminder),
    url(r'^setreminder/$',views.setreminder),
    url(r'^show_student_reminder/$',views.show_student_reminder),
    url(r'^show_faculty_reminder/$',views.show_faculty_reminder),
    url(r'^upload_data/$',views.upload_data),
    url(r'^email_request/$',views.email_request),
    url(r'^logout/$',views.logout),
    #url(r'^show_reminder/$',views.show_reminder),
    #url(r'^testgame/', TemplateView.as_view(template_name="../../../CE/1.txt"),name='txtgame'),
    #url(r'^validation/$',views.validation),
    #url(r'^upload/$',views.upload),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)