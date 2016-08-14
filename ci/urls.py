from django.conf.urls import url

from . import views

urlpatterns = [
    url('^login/$', views.login, name='login'),
    url('^logout/$', views.logout, name='logout'),
    url(r'^dashboard/(?P<dashboard_id>\d+)/', views.dashboard,
        name='dashboard'),
    url('^api/v1/metric/$', views.dashboard_metric, name='dashboard_metric'),
    url('', views.index, name='index'),
]
