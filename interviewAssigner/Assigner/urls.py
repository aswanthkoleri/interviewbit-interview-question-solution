from django.urls import path

from . import views
app_name = "Assigner"
urlpatterns = [
    path('create', views.index, name='index'),
    path('new',views.new, name='new'),
    path('list',views.list, name='list'),
]