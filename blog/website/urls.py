from django.conf.urls import url
from django.views.generic import TemplateView
from website import views

urlpatterns = [
        url(r'^post/(?P<slug>[-\w]+)/$', views.post_view, name='post-view'),
	url(r'^$', views.home, name='home'),
        url(r'^reg/$', views.registration, name='registration'),
]