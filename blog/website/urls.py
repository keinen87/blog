from django.conf.urls import url
from django.contrib.auth import views as auth_view
from django.views.generic import TemplateView
from website import views
from website.views import views_cbv_public

urlpatterns = [
        url(r'^demo/$', TemplateView.as_view(template_name='website/index.html'), name='demo'),
        url(r'^demo2/$', views_cbv_public.PostListView.as_view(), name='demo2'),
        url(r'^login/$', views.auth_login, name='auth_login'),
        #url(r'^login/$', auth_view.login, {'template_name':'website/login.html'}, name='auth_login'),
        url(r'^logout/$', views.logout, name='logout'),
        url(r'^account/post/new/$', views.PostCreateView.as_view(), name='account_post_create'),
        url(r'^account/edit/$', views.account_edit, name='account_edit'),
        url(r'^account/$', views.account, name='account'),
        url(r'^post/(?P<slug>[-\w]+)/edit/$', views.post_edit, name='post_edit'),
        #url(r'^post/(?P<slug>[-\w]+)/$', views.post_view, name='post'),
        url(r'^post/(?P<slug>[-\w]+)/$', views_cbv_public.PostDetailView.as_view(), name='post'),
        url(r'^$', views.home, name='home'),
        url(r'^reg/$', views.registration, name='registration'),
        url(r'^poll/$', views.poll, name='poll'),

]
