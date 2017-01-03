from django.conf.urls import url
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name = 'online_booking/index.html')),
    url(r'^customer_logged_in/$', views.logged, name='logged'),
    url(r'^confirm_login/$', views.confirm, name='confirm'),

]