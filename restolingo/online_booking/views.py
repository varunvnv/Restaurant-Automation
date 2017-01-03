from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from django.template import Context, loader

from .forms import CustomerForm, ConfirmForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from placeorder.models import *





def logged(request):
    username = "not logged in"

    if request.method == "POST":
        #Get the posted form
        MyLoginForm = CustomerForm(request.POST)
      
    if MyLoginForm.is_valid():
        username = MyLoginForm.cleaned_data['username']

    else:
        return HttpResponseRedirect('/online_booking/')
        
    return render(request, 'online_booking/logged_in.html', {"username" : username})



def confirm(request):

    password = 'wrong'

    if request.method == "POST":
        #Get the posted form
        MyLoginForm = ConfirmForm(request.POST)
      
    if MyLoginForm.is_valid():
        password = MyLoginForm.cleaned_data['manager_password']
        if password == 'varun':
            online_waiter = User.objects.get(username='online_waiter')  
            login(request,online_waiter)     # first is employee id and 2nd is table id
            tables = Table.objects.get(user_id=online_waiter.id) 
            redirect_url = '/placeorder/' + str(online_waiter.id)  + '/' +  str(tables.id)   
            #redirect_url = '/placeorder/12/5'
            return HttpResponseRedirect(redirect_url)
        else:
            return HttpResponseRedirect('/online_booking/')
    else:
        return HttpResponseRedirect('/online_booking/')

