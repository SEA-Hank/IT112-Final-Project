from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import EventType
from .config import navs

# Create your views here.


def error(request):
    return render(request, 'error.html', {"title": "error", "navs": navs})


def index(request):
    request.session["msg"] = "hi"
    return render(request, 'index.html', {"title": "list view", "navs": navs})


@login_required(login_url='login')
def welcome(request):
    return render(request, 'welcome.html', {"title": "welcome", "navs": navs, "username": request.user.username})


def typelist(request):
    try:
        msg = request.session.get("msg")
        if(msg != None):
            del request.session["msg"]
        eventTypeList = EventType.objects.all()
        count = eventTypeList.count()
        return render(request, 'typelist.html', {"title": "Event Type List", "navs": navs, "eventTypeList": eventTypeList, "count": count, "msg": msg})
    except:
        return redirect('error')


@require_http_methods(["POST"])
def typelistdelete(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % ('/todolist/login', '/todolist/typelist'))
    try:
        ids = request.POST.getlist("eventtype_ids", [])
        eventtypes = EventType.objects.filter(pk__in=ids)
        eventtypes.delete()
        request.session["msg"] = "delete success!"
        return redirect('typelist')
    except:
        return redirect('error')
