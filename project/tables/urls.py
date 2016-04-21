from django.conf.urls import include, url
from django.contrib import admin
from tables import views #gets all our view functions

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^form$', views.Form.as_view(), name='form'),
    # url(r'^register$', views.Register.as_view(), name='register'),
    # url(r'^login$', views.Login.as_view(), name='login'),
    # url(r'^logout$', views.Logout.as_view(), name='logout'),
]

