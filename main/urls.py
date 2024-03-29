from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("home/", views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
]
