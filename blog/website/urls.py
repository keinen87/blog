from django.conf.urls import url
from django.views.generic import TemplateView
from website import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
        url(r'^reg/$', TemplateView.as_view(template_name='website/reg.html')),
]
