from django.conf.urls import url
from todo.views import TodoView
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^$', TodoView.as_view()),
    url(r'(?P<pk>[0-9]+)/$/', TodoView.as_view())
]