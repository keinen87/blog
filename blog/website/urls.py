from django.conf.urls import url
#from django.views.generic import TemplateView
from website import views

urlpatterns = [
        url(r'^login/$', views.auth_login, name='auth_login'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^account/edit/$', views.account_edit, name='account_edit'),
        url(r'^account/$', views.account, name='account'),
        url(r'^post/(?P<slug>[-\w]+)/edit/$', views.post_edit, name='post_edit'),
        url(r'^post/(?P<slug>[-\w]+)/$', views.post_view, name='post'),
        url(r'^$', views.home, name='home'),
        url(r'^reg/$', views.registration, name='registration'),
        url(r'^poll/$', views.poll, name='poll'),

]
