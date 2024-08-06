"""
URL configuration for Collegeproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from userApp import views

urlpatterns = [
    path('admin/', include('adminApp.admin_urls')),

    path('',views.home),
    path('about_us/',views.about_us),
    path('history/',views.history),
    path('message/',views.message),
    path('leadership/',views.leadership),
    path('administration/',views.administration),
    path('faculty/',views.faculty),
    path('staff/',views.staff),
    path('why_study/',views.why_study),
    path('grievance/',views.grievance),
    path('anti_ragging/',views.anti_ragging),
    path('women/',views.women),
    path('opportunity/',views.opportunity),
    path('electoral/',views.electoral),
    path('harassment/',views.harassment),
    path('bcs/',views.bcs),
    path('ba/',views.ba),
    path('bba/',views.bba),
    path('bcom/',views.bcom),
    path('mcs/',views.mcs),
    path('mcom/',views.mcom),
    path('stulog/',views.stulog),
    path('faclog/',views.faclog),
    path('interstu/',views.interstu),
    path('nristu/',views.nristu),
    path('alumni/',views.alumni),
    path('new_sto/',views.new_sto),
    path('event/',views.event),
    path('gallery/',views.gallery),
    
    path('aabout_us/',views.aabout_us)








]
