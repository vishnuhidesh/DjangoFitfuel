from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.recommendFunction ),
    path("med/",views.medDiet),
    path("keto/",views.ketoDiet),
    path("paleo/",views.paleoDiet),
    path("dash/",views.dashDiet),
    path("zone/",views.zoneDiet),
    path("bal/",views.balDiet),
    path("inter/",views.interDiet),
]
