from django.conf.urls import include, patterns, url
from jsonrpc.backend.django import api

urlpatterns = patterns(
    '',
    url(r'', include(api.urls)),
    url(r'prefix', include(api.urls)),
)
