#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chase.mcnealy
#
# Created:     17/11/2015
# Copyright:   (c) chase.mcnealy 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]