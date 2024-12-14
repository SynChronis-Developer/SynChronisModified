from django.forms import ModelForm

from SynChronisApp.models import AttendanceTable, ClassTable, LeaveApplicationTable, LocationTable, LoginTable, NotesTable, StudentNoticeTable, StudentTable, SubjectTable, TeacherNoticeTable, TeacherTable, TimeTableTable


class LocationForm(ModelForm):
    class Meta:
        model = LocationTable
        fields = ['Location_name', 'latitude', 'longitude']
        
class TimeTableForm(ModelForm):
    class Meta:
        model = TimeTableTable
        fields = ['Class_name', 'Period', 'SubjectName', 'TeacherName', 'Day', 'StartTime', 'EndTime', ]
        
class ClassForm(ModelForm):
    class Meta:
        model = ClassTable
        fields = ['Class_name', 'TeacherName', 'Latitude', 'Longitude', 'Location_name', 'Department', 'Year', 'Semester']
        
class TeacherForm(ModelForm):
    class Meta:
        model = TeacherTable
        fields = ['TeacherName', 'Gender', 'Subject','Department','Qualification','Email', 'Phone_number',]
        
class SubjectForm(ModelForm):
    class Meta:
        model = SubjectTable
        fields = ['SubjectName', 'TeacherName', 'Course', 'Semester','Year_of_Syllabus']
        
class NotesForm(ModelForm):
    class Meta:
        model = NotesTable
        fields = ['SubjectName', 'Teacher', 'Class_name', 'Unit', 'Notes']
        
class LoginForm(ModelForm):
    class Meta:
        model = LoginTable
        fields = ['Username', 'Password']
        
class StudentForm(ModelForm):
    class Meta:
        model = StudentTable
        fields = ['StudentName', 'Gender', 'Admission_no','Department','Guardian_relation','Course','Address','Year','Semester','Age','Email', 'Phone_number','Class_name','Guardian_name','Guardian_phone','Date_of_birth','Blood_group']
        
class StudentNotificationForm(ModelForm):
    class Meta:
        model = StudentNoticeTable
        fields =['StudentName', 'Notice_Content', 'Notice_name', 'File_Attachment']
        
class TeacherNotificationForm(ModelForm):
    class Meta:
        model = TeacherNoticeTable
        fields =['TeacherName', 'Notice_Content', 'Notice_name',  'File_Attachment']
        

class LeaveApplicationForm(ModelForm):
    class Meta:
        model = LeaveApplicationTable
        fields = ['StudentName', 'Date', 'Reason', 'Status']
        