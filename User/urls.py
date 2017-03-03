from django.conf.urls import include, url
from views import *

urlpatterns = [
    url(r"login", login),
    url(r"404", r404),
    url(r"register", register),
    url(r"userValid", userValid),
    ]