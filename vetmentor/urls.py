from django.conf.urls import patterns, include
from mentor.views import LandingView
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', LandingView.as_view()),
    #(r'^accounts/', include('allauth.urls')),
    (r'^admin/', include(admin.site.urls)),
)
