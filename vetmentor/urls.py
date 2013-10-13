from django.conf.urls import patterns, include

urlpatterns = patterns('',
    (r'^accounts/', include('allauth.urls')),
)
