"""CV_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from CV_Management_System import settings
from process import views

urlpatterns = [
    path('',views.showindex,name='main'),
    path('Registration_page/',views.Registration_page,name='Registration_page'),
    path('user_registration/',views.Registration_page,name='user_registration'),
    path('otp_validate/',views.otp_validate,name='otp_validate'),
    path('validate/',views.validate,name='validate'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('welcome_page/',views.welcome_page,name='welcome_page'),
    path('validate_login/',views.validate_login,name='validate_login'),
    path('view_profile/',views.view_profile,name='view_profile'),
    path('delete_profile/',views.delete_profile,name='delete_profile'),
    path('about/',views.about,name='about'),
    path('logout/',views.logout,name='logout'),
    path('validate_profile/',views.validate_profile,name='validate_profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('save_industry/',views.save_industry,name='save_industry'),
    path('save_Profile/',views.save_Profile,name='save_Profile'),





]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
