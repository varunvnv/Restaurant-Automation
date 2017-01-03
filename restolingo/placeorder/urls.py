from django.conf.urls  import url

from . import views

urlpatterns = [
        url(r'^$', views.login_details, name='login_details'),
        url(r'^index/$', views.index, name='index'),
        url(r'^(?P<emp_id>[0-9]+)/$', views.detail, name='detail'),
        url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/$', views.menutype, name='menutype'),
        url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/$', views.menu, name='menu'),
        url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/(?P<menu_item>[\w-]+)/$', views.placeorder, name='placeorder'),
        url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/success/placed/$', views.placeordersuccess, name='placeordersuccess'),
		url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/success/cancelled/$', views.cancelOrder, name='cancelOrder'),
		url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/(?P<name>[\w-]+)/(?P<item_id>[0-9]+)/success/delete_item/$', views.deleteItem, name='deleteItem'),
        #url(r'^success/placed/$', views.placeordersuccess, name='placeordersuccess'),
	url(r'^view_active_orders/$', views.view_active_orders, name='active_orders'),
	url(r'^view_in_progress_orders/$', views.view_in_progress_orders, name='in_progress_orders'),
	url(r'^view_done_orders/$', views.view_done_orders, name='done_orders'),

	url(r'^view_active_orders/(?P<slug>[\w\-]+)/$', views.orders_detail, name='orders_detail'),
	url(r'^make_order_in_progress/(?P<slug>[\w\-]+)/$', views.make_order_in_progress, name='make_order_in_progress'),
	url(r'^view_in_progress_orders/(?P<slug>[\w\-]+)/$', views.in_progress_orders_detail, name='in_progress_orders_detail'),
	url(r'^make_order_done/(?P<slug>[\w\-]+)/$', views.make_order_done, name='make_order_done'),
    url(r'^notifications/(?P<iden>[0-9]+)/$', views.notifications, name='notifications'),
    url(r'^shift/(?P<shift>[0-9]+)/$', views.manage_shift, name='manage_shift'),
    url(r'^dirty/(?P<table_id>[0-9]+)/$', views.dirty, name='dirty'),
	url(r'^billdetails/(?P<tid>[0-9]+)/$', views.bill_details, name='bill_details'),
    url(r'^billdetails/(?P<tid>[0-9]+)/clear/$', views.clear_bills, name='clear_bill_details'),
]
