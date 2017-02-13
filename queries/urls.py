
from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',pnr_status,name='status'),


    #url(r'^home/$', pnr_status, name='status'),


]