from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("editprofile/", views.editProfileFunction),
    path("profile/", views.profileFunction)
    

]