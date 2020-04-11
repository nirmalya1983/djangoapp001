from django.urls import path

from . import views

urlpatterns = [
    path('ind_state',views.ind_states,name='indStates'),
    path('', views.index, name='index'),
]