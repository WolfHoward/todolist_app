from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from todos import views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^details/(?P<id>\w{0,50})/$', views.details),
    url(r'^add', views.add, name='add'),
    url(r'^api/$', views.TodoList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.TodoListDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
