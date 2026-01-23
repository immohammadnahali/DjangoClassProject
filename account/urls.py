# URL account
from . import views
from django.urls import path

urlpatterns = [

    path("", views.sign_up.as_view()),

]
