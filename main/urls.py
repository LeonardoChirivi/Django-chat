from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^register$', views.Register.as_view(), name='signup'),
    url(r'^logout', views.log_out, name='logout'),
]
