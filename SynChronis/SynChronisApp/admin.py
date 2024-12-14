from django.contrib import admin
from .models import LeaveApplicationTable, LocationTable, LoginTable, NotesTable, StudentNoticeTable, TeacherNoticeTable, TimeTableTable
from .models import TeacherTable
from .models import StudentTable
from .models import ClassTable
from .models import AttendanceTable

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(TeacherTable)
admin.site.register(StudentTable)
admin.site.register(ClassTable)
admin.site.register(AttendanceTable)
admin.site.register(LocationTable)
admin.site.register(TimeTableTable)
admin.site.register(NotesTable)
admin.site.register(LeaveApplicationTable)
admin.site.register(StudentNoticeTable)
admin.site.register(TeacherNoticeTable)