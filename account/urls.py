# URL account
from . import views
from django.urls import path

urlpatterns = [

    path("sign_up", views.sign_up.as_view()),
    path("login", views.login.as_view()),

]
