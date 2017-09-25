from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='log_reg_index'),
]
