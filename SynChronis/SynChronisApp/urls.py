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

from .views import AcceptTeacher, AddNoticeStudent, AddNoticeTeacher, Addnotes, AdminDashboard, AdminNotificationControl, ApproveLeaveApplication, Location, LoginPage, MainPage, RejectTeacher, SelectTime_Table, SendLeaveApplication, SettimeTable1, TimeTable, ViewNotes, ViewNoticeStudent, ViewNoticeTeacher, ViewTeacher,SettimeTable
urlpatterns = [
    path('', MainPage.as_view(), name='Main_Page'),
    path('Login_page/', LoginPage.as_view(), name='login'),
    path('View_Teacher/', ViewTeacher.as_view(), name='View_Teacher'),
    path('Time_Table/', TimeTable.as_view(), name='Time_Table'),
    path('Admin_Dashboard/', AdminDashboard.as_view(), name='Admin_Dashboard'),
    path('Location/', Location.as_view(), name='Location'),
    path('accept_teacher/<int:id>', AcceptTeacher.as_view(), name='accept_teacher'),
    path('reject_teacher/<int:id>', RejectTeacher.as_view(), name='reject_teacher'),
    path('SelectTime_Table/', SelectTime_Table.as_view(), name='SelectTime_Table'),
    path('set_time_table/<str:day>/<str:period>/<str:classname>', SettimeTable.as_view(), name='set_time_table'),
    path('SettimeTable1',SettimeTable1.as_view(),name='SettimeTable1'),
    path('Send_Leave_Application/', SendLeaveApplication.as_view(), name='Leave_Application'),
    path('Add_Notice_Teacher/', AddNoticeTeacher.as_view(), name='Add_Notice_Teacher'),
    path('View_Notice_Teacher/', ViewNoticeTeacher.as_view(), name='View_Notice_Teacher'),
    path('View_Leave_Application/', ApproveLeaveApplication.as_view(), name='View_Leave_Application'),
    path('Add_Notice_Student/', AddNoticeStudent.as_view(), name='Add_Notice_Student'),
    path('View_notice_student/', ViewNoticeStudent.as_view(), name='View_notice'),
    path('Add_Note/', Addnotes.as_view(), name='Add_Note'),
    path('View_Notes/', ViewNotes.as_view(), name='View_Notes'),
    path('Admin_Notification_Control/', AdminNotificationControl.as_view(), name='Admin_Notification_Control'),
]
