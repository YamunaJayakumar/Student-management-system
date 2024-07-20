"""
URL configuration for collegeproject project.

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
from django.urls import path
from collegeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a',views.adddep),
    path('treg',views.teacher_reg),
    path('student',views.student),
    path('sview',views.studentview),
    path('adminhome',views.adminhome),
    path('',views.home),
    path('approvest/<int:uid>',views.approvest),
    path('lg',views.logins),
    path('thome',views.teacherhome),
    path('shome',views.studenthome),
    path('logout',views.lgout),
    path('tview',views.teacherview),
    path('updateprofile',views.updateprofile),
    path('update_student/<int:uid>',views.update_student),
    path('updateprofile_t',views.updateprofile_t),
    path('update_teacher/<int:uid>',views.update_teacher),
    path('stview',views.tstudentview)
]
