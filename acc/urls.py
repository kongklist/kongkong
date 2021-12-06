from django.urls import path
from . import views

app_name = "acc"

urlpatterns = [
    path('', views.index, name="index"),
    path('signup', views.signup, name="signup"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('userlogout', views.userlogout, name="userlogout"),
    path('profile', views.profile, name="profile"),
    path('update', views.update, name="update"),
    path('remove', views.remove, name="remove")
]
