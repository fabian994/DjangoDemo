from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("c-rel", views.c_rel, name="c-rel"),
    path("c-norel", views.c_NOrel, name="c-norel"),
    path("r-rel", views.r_rel, name="r-rel"),
    path("r-norel", views.r_NOrel, name="r-norel"),
]