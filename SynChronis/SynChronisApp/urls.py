"""
URL configuration for SynChronis project.

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
from django.urls import  path

from SynChronisApp.views import AcceptTeacher, AdminDashboard, Location, LoginPage, MainPage, RejectTeacher, TimeTable, ViewTeacher

urlpatterns = [
    path('', MainPage.as_view(), name='Main_Page'),
    path('Login_page/', LoginPage.as_view(), name='login'),
    path('View_Teacher/', ViewTeacher.as_view(), name='View_Teacher'),
    path('Time_Table/', TimeTable.as_view(), name='Time_Table'),
    path('Admin_Dashboard/', AdminDashboard.as_view(), name='Admin_Dashboard'),
    path('Location/', Location.as_view(), name='Location'),
    path('accept_teacher/<int:id>', AcceptTeacher.as_view(), name='accept_teacher'),
    path('reject_teacher/<int:id>', RejectTeacher.as_view(), name='reject_teacher'),
]
