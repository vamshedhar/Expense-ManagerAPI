from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from transaction import views

urlpatterns = patterns('',
    url(r'^$', views.TransactionList.as_view()),
    url(r'^(?P<trip_id>[0-9]+)/$', views.TripTransactionList.as_view()),
    url(r'^(?P<trip_id>[0-9]+)/(?P<user_id>[0-9]+)/$', views.TripUserTransactionList.as_view()),
    url(r'^view/(?P<pk>[0-9]+)/$', views.TransactionDetails.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)