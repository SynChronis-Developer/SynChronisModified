from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    
class TeacherTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE,null=True, blank=True)
    TeacherName = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Phone_number =   models.BigIntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Qualification = models.CharField(max_length=50, null=True, blank=True)
    
class ClassTable(models.Model):
    TeacherName= models.ForeignKey(TeacherTable, on_delete=models.CASCADE, null=True, blank=True)
    Class_name = models.CharField(max_length=50, null=True, blank=True)
    Latitude = models.CharField(max_length=50, null=True, blank=True)
    Longitude = models.CharField(max_length=50, null=True, blank=True)
    Location_name = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Year = models.CharField(max_length=50, null=True, blank=True)
    Semester = models.CharField(max_length=50, null=True, blank=True)

class StudentTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE, null=True, blank=True)
    Class_name = models.ForeignKey(ClassTable, on_delete=models.CASCADE, null=True, blank=True)
    StudentName = models.CharField(max_length=50, null=True, blank=True)
    Admission_no = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Semester = models.CharField(max_length=50, null=True, blank=True)
    Year = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField( null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    Date_of_birth = models.DateField( null=True, blank=True)
    Blood_group = models.CharField(max_length=50, null=True, blank=True)
    Guardian_name = models.CharField(max_length=50, null=True, blank=True)
    Guardian_relation = models.CharField(max_length=50, null=True, blank=True)
    Guardian_phone = models.BigIntegerField( null=True, blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Phone_number = models.BigIntegerField( null=True, blank=True)

class AttendanceTable(models.Model):
    StudentName= models.ForeignKey(StudentTable, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.DateField( null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)
    Attendance = models.IntegerField( null=True, blank=True)



class TimeTableTable(models.Model):
    Class_name = models.ForeignKey(ClassTable, on_delete=models.CASCADE, null=True, blank=True)
    Period = models.CharField(max_length=50, null=True, blank=True)
    SubjectName = models.CharField(max_length=50, null=True, blank=True)
    TeacherName =models.ForeignKey(TeacherTable, on_delete=models.CASCADE, null=True, blank=True)
    Day = models.CharField(max_length=50 ,null=True, blank=True)
    StartTime = models.TimeField( null=True, blank=True)
    EndTime = models.TimeField( null=True, blank=True)
    
    
class LocationTable(models.Model):
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    Location_name = models.CharField(max_length=50, null=True, blank=True)
    
class SubjectTable(models.Model):
    SubjectName = models.CharField(max_length=50, null=True, blank=True)
    TeacherName = models.ForeignKey(TeacherTable, on_delete=models.CASCADE, null=True, blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Year_of_Syllabus = models.DateField(null=True, blank=True)  # Corrected to remove max_length
    Semester = models.CharField(max_length=50, null=True, blank=True)


class NotesTable(models.Model):
    SubjectName = models.ForeignKey(SubjectTable, on_delete=models.CASCADE, null=True, blank=True)
    Teacher =models.ForeignKey(TeacherTable, on_delete=models.CASCADE, null=True, blank=True)
    Class_name = models.ForeignKey(ClassTable, on_delete=models.CASCADE, null=True, blank=True)
    Unit = models.CharField(max_length=50, null=True, blank=True)
    Notes = models.CharField(max_length=50, null=True, blank=True)
    
class LeaveApplicationTable(models.Model):
    StudentName = models.ForeignKey(StudentTable, on_delete=models.CASCADE, null=True, blank=True)
    Date = models.DateField( null=True, blank=True)
    Reason = models.CharField(max_length=50, null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)
    
class StudentNoticeTable(models.Model):
    StudentName = models.ForeignKey(StudentTable, on_delete=models.CASCADE, null=True, blank=True)
    Notice_name = models.CharField(max_length=50, null=True, blank=True)
    Notice_Content = models.CharField(max_length=50, null=True, blank=True)
    Date = models.DateField( null=True, blank=True)
    File_Attachment = models.FileField(max_length=50, null=True, blank=True)
    
class TeacherNoticeTable(models.Model):
    TeacherName = models.ForeignKey(TeacherTable, on_delete=models.CASCADE, null=True, blank=True)
    Notice_name = models.CharField(max_length=50, null=True, blank=True)
    Notice_Content= models.CharField(max_length=50, null=True, blank=True)
    Date = models.DateField(auto_now_add=True, null=True, blank=True)
    File_Attachment = models.FileField(upload_to='File/', null=True, blank=True)
    