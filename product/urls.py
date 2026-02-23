# URL PRODUCT
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index),
    path("article/", views.article),
    path("category/", views.category),
    path("contact_us/", views.contact_us),
    path("error404/", views.error404),
    path("search/", views.search),
    path("teach/", views.teach),
    path("Futurecoursess/<str:slug>", views.Fc, name="Fc"),
    path("product/<str:slug>", views.dkp, name="dkp"),
    path("article/art-<str:slug>", views.art, name="art"),

]
