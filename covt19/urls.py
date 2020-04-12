from django.urls import path

from . import views

urlpatterns = [
    path('ind_state',views.ind_states,name='indStates'),
    path('ind_test',views.ind_test,name='indTest'),
    path('', views.index, name='index'),
]