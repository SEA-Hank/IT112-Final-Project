from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .config import navs

# Create your views here.


def index(request):
    return render(request, 'index.html', {"title": "list view", "navs": navs})


@login_required(login_url='/todolist/login')
def welcome(request):
    return render(request, 'welcome.html', {"title": "welcome", "navs": navs, "username": request.user.username})
