from django.urls import re_path
from bookshop import views

urlpatterns = [
        re_path('^$', views.index),
        re_path(r"^just_url/(?P<id_book>[\d]+)/$", views.comment_handler, name='comment_url'),
        re_path('^world/$', views.hello),
        ]
