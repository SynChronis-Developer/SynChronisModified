from django.db import models

# Create your models here.

class LoginTable(models.Model):
    Username = models.CharField(max_length=50, null=True, blank=True)
    Password = models.CharField(max_length=50, null=True, blank=True)
    Type = models.CharField(max_length=50, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    
class TeacherTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Phone_number =   models.BigIntegerField(null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Qualification = models.CharField(max_length=50, null=True, blank=True)

class StudentTable(models.Model):
    LOGIN = models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    Name = models.CharField(max_length=50, null=True, blank=True)
    Admission_no = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Year = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField( null=True, blank=True)
    Gender = models.CharField(max_length=50, null=True, blank=True)
    Date_of_birth = models.DateField( null=True, blank=True)
    Blood_group = models.CharField(max_length=50, null=True, blank=True)
    Guardian_name = models.CharField(max_length=50, null=True, blank=True)
    Guardian_relation = models.CharField(max_length=50, null=True, blank=True)
    Guardian_phone_number = models.BigIntegerField( null=True, blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Phone_number = models.BigIntegerField( null=True, blank=True)

class AttendanceTable(models.Model):
    STUDENT = models.ForeignKey(StudentTable, on_delete=models.CASCADE)
    Date = models.DateField( null=True, blank=True)
    Status = models.CharField(max_length=50, null=True, blank=True)
    Attendance = models.IntegerField( null=True, blank=True)

class ClassTable(models.Model):
    TEACHER = models.ForeignKey(TeacherTable, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50, null=True, blank=True)
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    Location_name = models.CharField(max_length=50, null=True, blank=True)
    Department = models.CharField(max_length=50, null=True, blank=True)
    Year = models.CharField(max_length=50, null=True, blank=True)

class TimeTable(models.Model):
    Class_name = models.ForeignKey(ClassTable, on_delete=models.CASCADE)
    Period = models.CharField(max_length=50, null=True, blank=True)
    Subject = models.CharField(max_length=50, null=True, blank=True)
    Teacher =models.ForeignKey(TeacherTable, on_delete=models.CASCADE)
    Day = models.CharField(max_length=50, null=True, blank=True)
    Semester = models.CharField(max_length=50, null=True, blank=True)
    
class LocationTable(models.Model):
    latitude = models.CharField(max_length=50, null=True, blank=True)
    longitude = models.CharField(max_length=50, null=True, blank=True)
    Location_name = models.CharField(max_length=50, null=True, blank=True)
    