"""
URL configuration for fitfuel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logreg.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('', include('userprofile.urls')),
    path('', include('foodmodule.urls')),
    path('diets/', include('diets.urls')),
    path('',views.landingFunction),
    path('navbar/',views.navbarFunction),
    path('charts/',views.chartsFunction),
    path('intake/',views.intakeFunction),
    path('intellirec/',views.recommendFunction),
    path('health/',views.healthFunction),
    path('blank/',views.blankFunction),



]
