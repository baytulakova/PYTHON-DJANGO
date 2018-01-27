from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^site6/', include('polls.urls')),
    url(r'^site5/', include('polls.urls')),
    url(r'^site4/', include('polls.urls')),
    url(r'^site3/', include('polls.urls')),
    url(r'^site2/',include('polls.urls')),
    url(r'^site1/',include('polls.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
