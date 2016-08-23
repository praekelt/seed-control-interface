from django.conf.urls import url

from . import views

urlpatterns = [
    url('^login/$', views.login, name='login'),
    url('^logout/$', views.logout, name='logout'),
    url(r'^dashboard/(?P<dashboard_id>\d+)/', views.dashboard,
        name='dashboard'),
    url('^api/v1/metric/$', views.dashboard_metric, name='dashboard_metric'),
    url('^identities/$', views.identities, name='identities'),
    url(r'^identities/(?P<identity>[^/]+)/$', views.identity,
        name='identities-detail'),
    url('^registrations/$', views.registrations, name='registrations'),
    url(r'^registrations/(?P<registration>[^/]+)/$', views.registration,
        name='registrations-detail'),
    url('^subscriptions/$', views.subscriptions, name='subscriptions'),
    url(r'^subscriptions/(?P<subscription>[^/]+)/$', views.subscription,
        name='subscriptions-detail'),
    url('^services/$', views.services, name='services'),
    url(r'^services/(?P<service>[^/]+)/$', views.service,
        name='services-detail'),
    url('^denied/$', views.denied, name='denied'),
    url('^404/$', views.denied, name='not_found'),
    url('', views.index, name='index'),
]
