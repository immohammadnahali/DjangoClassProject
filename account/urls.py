# URL account
from . import views
from django.urls import path

urlpatterns = [

    path("sign_up/", views.sign_up.as_view(), name="sign_up"),
    path("login/", views.login.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path('panel_user/', views.panel_user, name='panel_user'),

]
