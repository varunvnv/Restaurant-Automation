URLS
======
	THIS IS THE urlS DOCUMENTATION PAGE
This file is used to map urls to views by using regular expressions to match strings.

**url(r'^$', views.login_details, name='login_details')**   
*********************************************************
Maps the empty url with the login_details view 

**url(r'^index/$', views.index, name='index')**    
*********************************************
Maps the index url with the index view

**url(r'^(?P<emp_id>[0-9]+)/$', views.detail, name='detail')**  
******************************************************************
Maps the employee if url with detail view

**url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/$', views.menutype, name='menutype')**
************************************************************************************************************
Maps employee_id/table_id url with the menutype view

**url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/$', views.menu, name='menu')** 
************************************************************************************************************
Maps the  employee_id/table_id/menu_type url with the menu view

**url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/(?P<menu_item>[\w-]+)/$', views.placeorder, name='placeorder')**   
*********************************************************************************************************************************
Maps the employee_id/table_id/menu_type/menu)item with the placeorder view

**url(r'^(?P<emp_id>[0-9]+)/(?P<table_id>[0-9]+)/(?P<menu_type>[\w-]+)/(?P<random>[\w-]+)/(?P<rand>[\w-]+)/$', views.placeordersuccess, name='placeordersuccess')**  
******************************************************************************************************************************
Maps the employee_id/table_id/menu_type/menu_item/random_number_random_number with the placeordersuccess view

**url(r'^view_active_orders/$', views.view_active_orders, name='active_orders')**    
************************************************************************************************************
Maps the view_active_orders url with the view_active_orders view 

**url(r'^view_in_progress_orders/$', views.view_in_progress_orders, name='in_progress_orders')**
***********************************************************************************************************
Maps the view_in_progress_orders url with the view_in_progress_orders view

**url(r'^view_done_orders/$', views.view_done_orders, name='done_orders')**     
*************************************************************************************
Maps the view_done_orders url with the view_done_orders view

**url(r'^view_active_orders/(?P<slug>[\w\-]+)/$', views.orders_detail, name='orders_detail')**
*********************************************************************************************************
Maps  the view_active_orders/slug url with the orders_detail view 

**url(r'^make_order_in_progress/(?P<slug>[\w\-]+)/$', views.make_order_in_progress, name='make_order_in_progress')**  
*************************************************************************************************************************
Maps the make_order_in_progress/slug url with the make_order_in_progress view

**url(r'^view_in_progress_orders/(?P<slug>[\w\-]+)/$', views.in_progress_orders_detail, name='in_progress_orders_detail')** 
*******************************************************************************************************
Maps the  view_in_progress_orders/slug url with the orders_detail view 

**url(r'^make_order_done/(?P<slug>[\w\-]+)/$', views.make_order_done, name='make_order_done')**   
*******************************************************************************************************
Maps the make_order_done/slug url with the make_order_done view

**url(r'^notifications/(?P<iden>[0-9]+)/$', views.notifications, name='notifications'),
*******************************************************************************************************
Maps the notifications/slug url with the notifications view

**url(r'^shift/(?P<shift>[0-9]+)/$', views.manage_shift, name='manage_shift'),
*******************************************************************************************************
Maps the manage_shift/slug url with the manage_shift view
  
**url(r'^dirty/(?P<table_id>[0-9]+)/$', views.dirty, name='dirty'),
*******************************************************************************************************
Maps the dirty/slug url with the dirty view

**url(r'^billdetails/(?P<tid>[0-9]+)/$', views.bill_details, name='bill_details'),
*******************************************************************************************************
Maps the bill_details/slug url with the bill_details view
    
**url(r'^billdetails/(?P<tid>[0-9]+)/clear/$', views.clear_bills, name='clear_bill_details'),
*******************************************************************************************************
Maps the clear_bills/slug url with the clear_bills view

