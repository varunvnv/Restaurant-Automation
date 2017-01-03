from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from placeorder.models import *
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

from placeorder.views import access_restricted



@csrf_exempt
@login_required
def index(request):  # TO DO: add authorization
    if access_restricted(request, 'busboy'):
        name = request.user.username
        varun = User.objects.get(username=name)
        shift = Shift.objects.get(user_id=varun.id)

        if request.method == 'GET':
            table_list = Table.objects.all()
            template = loader.get_template('busboy/tables.html')
            context = Context({'table_list': table_list, 'shift':shift, 'name':name})
            output = template.render(context)
            return HttpResponse(output)
        if request.method == 'POST':
            table_id = request.POST.get("table_id", "")
            table_to_update = Table.objects.get(id=table_id)
            table_to_update.status = 'available'
            table_to_update.save()
            table_list = Table.objects.all()
            template = loader.get_template('busboy/tables.html')
            context = Context({'table_list': table_list, 'shift':shift, 'name':name})
            output = template.render(context)
            return HttpResponse(output)
    else:
        raise Http404("You are not authorized to view this page")
