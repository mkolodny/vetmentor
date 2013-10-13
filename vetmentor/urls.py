from django.conf.urls import patterns, include
from mentor.views import LandingView

urlpatterns = patterns('',
    (r'', LandingView.as_view()),
    (r'^accounts/', include('allauth.urls')),
)
