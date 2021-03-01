from django.shortcuts import render

# Create your views here.


def getNav():
    nav = [{"label": "List View", "url": "index"},
           {"label": "Event Type", "url": "index"},
           {"label": "Add Event", "url": "index"},
           {"label": "Login", "url": "index"},
           {"label": "logout", "url": "index"}]
    return nav


def index(request):
    return render(request, 'index.html', {"title": "list view", "navs": getNav()})
