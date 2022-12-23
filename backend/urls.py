from django.urls import path
from .views import *

urlpatterns = [
    path('', index ,name='index' ),
    path('<slug:slug>/', article , name='article'),
    path('contact', contact, name='contact'),
]