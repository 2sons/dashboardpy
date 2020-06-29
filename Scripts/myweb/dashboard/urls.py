from django.conf.urls import url
from dashboard import views

urlpatterns = [
    url(r'^contact', views.contact),
    url(r'^about', views.about),
]