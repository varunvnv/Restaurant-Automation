from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from django.contrib.auth import  (
        get_user, get_user_model, logout)

from django.http import  HttpResponse
from django.shortcuts import render, redirect

@login_required
def home(request):
    if request.user.is_superuser:
        return HttpResponseRedirect('/admin')
    username = request.user.username
    group_name=request.user.groups.values_list('name',flat=True)
    if 'waiter' in group_name:
        return HttpResponseRedirect('/placeorder/index')
    elif 'chef' in group_name:
        return HttpResponseRedirect('/placeorder/view_active_orders')
    elif 'busboy' in group_name:
        return HttpResponseRedirect('/busboy')
    elif 'host' in group_name:
        return HttpResponseRedirect('/host')
    else:
        return HttpResponse("You are not an authorized user. Only \
                            a " + group_name[0] + "can access this page" )




def dispatch(self, request, *args, **kwargs):
    return super().dispatch(request,*args,**kwargs)
