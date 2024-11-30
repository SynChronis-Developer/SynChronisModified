from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from SynChronisApp.form import LocationForm

from .models import ClassTable, LoginTable, TeacherTable ,TimeTableTable

# Create your views here.

class LoginPage(View):
    def get(self, request):
        return render(request, 'adminlog.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            obj = LoginTable.objects.get(Username=username, Password=password)
            if obj.Type == 'Admin':
                return render(request, 'admindashboard.html')
            else:
                return HttpResponse('''<script>alert('Invalid Credentials');window.location.href='/Login_page';</script>''')
        except LoginTable.DoesNotExist:
            messages.error(request, 'Invalid username or password')
            
        


class ViewTeacher(View):
    def get(self, request):
        te=TeacherTable.objects.all()
        return render(request, 'viewteacher.html',{'te':te})
    
class AcceptTeacher(View):
    def get(self, request, id):
        obj = TeacherTable.objects.get(id=id)
        print("ACC",obj.LOGIN.status)
        obj.LOGIN.status = 'Accept'
        obj.LOGIN.save()
        print("ACC",obj.LOGIN.status)
        return redirect('View_Teacher')

class RejectTeacher(View):
    def get(self, request, id):
        obj = TeacherTable.objects.get(id=id)
        print("RE",obj.LOGIN.status)
        obj.LOGIN.status = 'Reject'
        obj.LOGIN.save()
        return redirect('View_Teacher')
    
class TimeTable(View):
    def get(self, request):
       
        tt=TimeTableTable.objects.all()
        return render(request, 'timetable.html',{'tt':tt})
    

class SettimeTable(View):
    def get(self, request,day,period):
        print(day,period)
        tt=TimeTableTable.objects.all()
        return render(request, 'settimetable.html',{'tt':tt,'day':day,'period':period})
    
class MainPage(View):
    def get(self, request):
        return render(request, 'mainpage.html')

class AdminDashboard(View):
    def get(self, request):
        return render(request, 'admindashboard.html')
    
class Location(View):
    def get(self, request):
        return render(request, 'location.html')
    def post(self, request):
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert('location added successfully');window.location.href='/Location';</script>''')
       
class SelectTime_Table(View):
    def get(self, request):
        return render(request, 'selecttimetable.html')
        