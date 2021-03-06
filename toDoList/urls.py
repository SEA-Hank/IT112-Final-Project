from django.urls import path
from django.contrib.auth import views as auth_views
from .config import navs

from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name='login.html',
        extra_context={"title": "login", "navs": navs}),
        name='login'),

    path('logout', auth_views.LogoutView.as_view(
        template_name='logout.html',
        extra_context={"title": "logout", "navs": navs}),
        name='logout'),

    path('error', views.error, name='error'),

    path('', views.index, name='index'),
    path('welcome', views.welcome, name="welcome"),

    path('typelist', views.typelist, name="typelist"),
    path('typelistdelete', views.typelistdelete, name="typelistdelete"),
    path('typesave/<int:reqid>', views.typesave, name="typesave"),
    path('typesave', views.typesave, name="typesave"),

    path('eventsave/<int:reqid>', views.eventsave, name="eventsave"),
    path('eventsave', views.eventsave, name="eventsave")
]
