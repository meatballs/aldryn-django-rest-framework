# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include


urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
