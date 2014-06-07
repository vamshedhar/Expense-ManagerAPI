from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from trip import views

urlpatterns = patterns('',
    url(r'^$', views.TripList.as_view()),
    url(r'^(?P<trip_id>[0-9]+)/$', views.TripMembersList.as_view()),
    url(r'^(?P<trip_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.TripMemberDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)