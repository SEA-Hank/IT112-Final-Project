from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='addevent'),
    path('', views.index, name='login'),
    path('', views.index, name='logout')
]
