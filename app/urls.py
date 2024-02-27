"""
URL configuration for app project.

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
from CBV import views
from FBV.views import getteacher, getteacherbyid, addteacher, updatedata, deleteteacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student', views.StudentViews.as_view()),
    path('student/<int:pk>/', views.StudentViews.as_view()),
    path('getteacher/', getteacher),
    path('getteacherbyid/<int:pk>', getteacherbyid),
    path('addteacher',addteacher),
    path('update/<int:pk>', updatedata),
    path('deleteteacher/<int:pk>', deleteteacher)
]
