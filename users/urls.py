from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from users import views

urlpatterns = patterns('',
    url(r'^$', views.UsersList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.UserDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)