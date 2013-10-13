from django.conf.urls import patterns, include
from mentor.views import LandingView, SignupView
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    (r'^$', LandingView.as_view()),
    (r'^signup$', SignupView.as_view()),
    #(r'^accounts/', include('allauth.urls')),
    (r'^admin/', include(admin.site.urls)),
)
