from django.urls import path
from app2.views import *

app_name = 'app2'

urlpatterns = [
    path('app2_htmlpage/',app2_htmlpage,name='app2_htmlpage'),
]