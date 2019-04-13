from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='leads'),
    path('noncontact',views.noncontact,name='noncontact'),
    path('followup',views.followup,name='followup'),
    path('walkin',views.walkin,name='walkin'),
]