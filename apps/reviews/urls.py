from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/(?P<book_id>\d+)$', views.book_detail, name='book_detail'),
    url(r'^books/add$', views.add_book, name='add_book'),
    url(r'^users/(?P<user_id>\d+)$', views.user_detail, name='user_detail'),
]
