from django.urls import path
from app1.views import *

app_name = 'app1'

urlpatterns = [
    path('app1_htmlpage/',app1_htmlpage,name='app1_htmlpage'),
]