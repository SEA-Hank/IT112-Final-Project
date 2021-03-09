from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import EventType, Event
from .config import navs
from .form import EventTypeForm, EventForm

# Create your views here.


def error(request):
    return render(request, 'error.html', {"title": "error", "navs": navs})


def index(request):
    try:
        msg = request.session.get("msg")
        if(msg != None):
            del request.session["msg"]
        eventlist = Event.objects.all()
        eventTypeCount = EventType.objects.count()
        return render(request, 'index.html', {"title": "Event List", "navs": navs, "eventlist": eventlist, "eventTypeCount": eventTypeCount, "msg": msg})
    except:
        return redirect('error')


@login_required(login_url='login')
def eventsave(request, reqid=None):
    try:
        eventObj = None
        if reqid != None:
            eventObj = get_object_or_404(Event, pk=reqid)
        if request.method == "GET":
            form = EventForm(instance=eventObj)
            return render(request, 'eventsave.html', {'form': form, "navs": navs, "showDel": eventObj != None})

        if request.method == 'POST':
            action = request.POST.get("action")
            if action == "delete":
                eventObj.delete()
                return redirectTo(request, "index", "delete success!")
            if action == "save":
                if eventObj == None:
                    eventObj = Event(createdByUser=request.user)
                form = EventForm(request.POST, instance=eventObj)
                if form.is_valid():
                    form.save()
                    return redirectTo(request, "index", "save success!")
        return redirect("index")
    except:
        return redirect('error')


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
        return redirectTo(request, "typelist", "delete success!")
    except:
        return redirect('error')


@login_required(login_url='login')
def typesave(request, reqid=None):
    try:
        eventtypeObj = None
        if reqid != None:
            eventtypeObj = get_object_or_404(EventType, pk=reqid)
        if request.method == "GET":
            form = EventTypeForm(instance=eventtypeObj)
            return render(request, 'typesave.html', {'form': form, "navs": navs})

        if request.method == 'POST':
            if eventtypeObj == None:
                eventtypeObj = EventType(createdByUser=request.user)
            form = EventTypeForm(request.POST, instance=eventtypeObj)
            if form.is_valid():
                form.save()
                return redirectTo(request, "typelist", "save success!")
            return render(request, 'typesave.html', {'form': form, "navs": navs})
    except:
        return redirect('error')


def redirectTo(request, url, msg=None):
    if(msg != None):
        request.session["msg"] = msg
    return redirect(url)
