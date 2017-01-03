from itertools import chain

from django.shortcuts import render
from datetime import datetime, timedelta
from django.db import models
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.


from django.http import HttpResponse
from django.template import Context, loader
from .models import *

#total = 0

def access_restricted(request, users_group):
    group_name = request.user.groups.values_list('name', flat=True)
    if users_group in group_name:
        return True
    else:
        return False


@login_required
def bill_details(request, tid):
    if access_restricted(request, 'waiter'):
        total=0
        bill = OrderList.objects.filter(status=1, table_id=tid)
        for i in bill.iterator():
            item=Item.objects.get(name=i.item_name)
            total=total + item.price
        context = {'bill':bill,'tid':tid,'total':total}
        return render(request, 'placeorder/bill_details.html', context)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def detail(request, emp_id):
    if access_restricted(request, 'waiter'):
        tables = Table.objects.filter(user_id=emp_id)
        s = Shift.objects.get(user_id=emp_id)
        shift = s.id
        context = {'tables': tables, 'emp_id': emp_id, 'shift':shift}
        return render(request, 'placeorder/details.html', context)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def index(request):
    if access_restricted(request, 'waiter'):
        name=request.user.username
        varun = User.objects.get(username=name)
        s = Shift.objects.get(user_id=varun.id)
        shift = s.id
        context = {'name': varun, 'shift':shift}
        return render(request, 'placeorder/index.html', context)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def menutype(request, emp_id, table_id):
    if access_restricted(request, 'waiter'):
        try:
            menu_list = Item.objects.order_by('type')
        except Item.DoesNotExist:
            raise Http404("Menu does not exist")
        context = {'menu_list': menu_list, 'emp_id': emp_id, 'table_id': table_id}
        return render(request, 'placeorder/menu.html', context)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def menu(request, emp_id, table_id, menu_type):
    if access_restricted(request, 'waiter'):
        try:
            menu_list = Item.objects.filter(type=menu_type)
        except Item.DoesNotExist:
            raise Http404("Menu does not exist")
        context = {'menu_list': menu_list, 'emp_id': emp_id, 'table_id': table_id, 'menu_type': menu_type}
        return render(request, 'placeorder/menuitem.html', context)
    else:
        raise Http404("You are not authorized to view this page")


@login_required
def placeorder(request, emp_id, table_id, menu_type, menu_item):
    if access_restricted(request, 'waiter'):
        #global total
        total=0 
        menuitem = Item.objects.get(name=menu_item)
        table=Table.objects.get(id=table_id)
        todo = DynamicOrder(item_name=menuitem.name, cost=menuitem.price,table_id=table)
        todo.save()
        list = DynamicOrder.objects.filter(table_id=table_id)
        for i in list.iterator():
            total=total + i.cost
        # menuitem= Item.objects.all()
        context = {'list': list, 'emp_id': emp_id, 'table_id': table_id, 'menu_type': menu_type, 'total': total}
        return render(request, 'placeorder/placeorder.html', context)
    else:
        raise Http404("You are not authorized to view this page")


@login_required
def placeordersuccess(request, emp_id, table_id, menu_type):
    if access_restricted(request,'waiter'):
        # def placeordersuccess(request):
        #global total
        tot=0		
        todo = DynamicOrder.objects.filter(table_id=table_id)
        for i in todo.iterator():
            tot=tot + i.cost
        emp = User.objects.get(id=emp_id)
        tab = Table.objects.get(id=table_id)
        # date = models.DateField(_("Date"), default=datetime.date.today)
        insert_order = Order(user_id=emp, table_id=tab, total = tot )
        insert_order.save()
        #total = 0

        last_order = Order.objects.all().last()
        for i in todo.iterator():
            menu_item = Item.objects.get(name=i.item_name)
            OrderItem.objects.create(order_id=last_order, item_id=menu_item)
        for i in todo.iterator():
            pin = Item.objects.get(name=i.item_name)
            order_list = OrderList(order_id=last_order,item_name=pin,table_id=tab)
            order_list.save()
        todo.delete()
        
        return render(request, 'placeorder/orderplaced.html', {'emp_id': emp_id, 'table_id': table_id})
    else:
        raise Http404("You are not authorized to view this page")


@login_required
def cancelOrder(request, emp_id, table_id, menu_type):
    if access_restricted(request,'waiter'):
        todo = DynamicOrder.objects.filter(table_id=table_id)
        todo.delete()
        total=0
        list = DynamicOrder.objects.filter(table_id=table_id)
        # menuitem= Item.objects.all()
        context = {'list': list, 'emp_id': emp_id, 'table_id': table_id, 'menu_type': menu_type, 'total': total}
        return render(request, 'placeorder/placeorder.html', context)
    else:
        raise Http404("You are not authorized to view this page")

@login_required 
def deleteItem(request, emp_id, table_id, menu_type,name, item_id):
    if access_restricted(request,'waiter'):
        menuitem = Item.objects.get(name=name)
        todo = DynamicOrder.objects.filter(table_id=table_id, id=item_id)
        todo.delete()
        #total=total + menuitem.price
        list = DynamicOrder.objects.filter(table_id=table_id)
        # menuitem= Item.objects.all()
        context = {'list': list, 'emp_id': emp_id, 'table_id': table_id, 'menu_type': menu_type}
        return render(request, 'placeorder/placeorder.html', context)
    else:
        raise Http404("You are not authorized to view this page")
    
@login_required
def login_details(request):
    if access_restricted(request,'waiter'):
        return render(request, 'placeorder/login_waiter.html', {})
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def view_active_orders(request):  # view for all the active orders
    if access_restricted(request, 'chef'):
        order_list = Order.objects.filter(status=0).order_by('order_date')
        template = loader.get_template('placeorder/view_active_orders.html')
        context = Context({'order_list': order_list})
        output = template.render(context)
        return HttpResponse(output)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def view_in_progress_orders(request):  # view for all the active orders
    if access_restricted(request, 'chef'):
        order_list = Order.objects.filter(status=1).order_by('order_date')
        template = loader.get_template('placeorder/view_in_progress_orders.html')
        context = Context({'order_list': order_list})
        output = template.render(context)
        return HttpResponse(output)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def orders_detail(request, slug):  # view for watching each active order separately and making it in progress
    if access_restricted(request, 'chef'):
        order = Order.objects.get(slug__iexact=slug)
        template = loader.get_template('placeorder/order_detail.html')    
        context = Context({'order': order})
        return HttpResponse(template.render(context))
    else:
        raise Http404("You are not authorized to view this page")


@login_required
def make_order_in_progress(request, slug):
    if access_restricted(request, 'chef'):
        order = Order.objects.get(slug__iexact=slug)
        order.status = 1
        order.save()
        template = loader.get_template('placeorder/success.html')
        context = Context({'order_id': order.id})
        return HttpResponse(template.render(context))
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def in_progress_orders_detail(request, slug):
    if access_restricted(request, 'chef'):
        order = Order.objects.get(slug__iexact=slug)
        template = loader.get_template('placeorder/order_detail.html')
        context = Context({'order': order})
        return HttpResponse(template.render(context))
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def make_order_done(request, slug):
    if access_restricted(request, 'chef'):
        order = Order.objects.get(slug__iexact=slug)
        order.status = 2
        order.save()
        template = loader.get_template('placeorder/success.html')
        context = Context({'order_id': order.id})
        return HttpResponse(template.render(context))
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def view_done_orders(request):  # view for all the active orders
    if access_restricted(request, 'chef'):
        o1 = Order.objects.filter(status=2).order_by('order_date')
        o2 = Order.objects.filter(status=3).order_by('order_date')
        order_list = list(chain(o1, o2))
        template = loader.get_template('placeorder/view_done_orders.html')
        context = Context({'order_list': order_list})
        output = template.render(context)
        return HttpResponse(output)
    else:
        raise Http404("You are not authorized to view this page")


@login_required
def notifications(request, iden):
    if access_restricted(request, 'waiter'):
        if (request.method == 'POST'):
            stat = Order.objects.get(pk=iden)
            stat.status = 3
            stat.save()
        item = Order.objects.filter(status=2)
        context = {'item': item}
        return render(request, 'placeorder/notifications.html', context)
    else:
        raise Http404("You are not authorized to view this page")

@login_required
def manage_shift(request, shift):
    #if (request.method == 'POST'):
        stat = Shift.objects.get(pk=shift)
        context = {'stat': stat}
        return render(request, 'placeorder/shifts.html', context)


@login_required
def dirty(request, table_id):
    table = Table.objects.get(pk=table_id)
    table.status='dirty'
    table.save()
    return HttpResponse("Table status successfully updated to dirty!!")
    
@login_required
def clear_bills(request, tid):
    bill = OrderList.objects.filter(status=1, table_id=tid)
    for i in bill.iterator():
        i.status=0
        i.save()
    return HttpResponse("Items Cleared")
