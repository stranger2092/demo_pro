from django.db import models
from rest_framework import pagination
# Create your models here.
    

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    # teacher = models.ForeignKey(Teacher, related_name='students', on_delete=models.CASCADE)
    rollno = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class LeaveForm(models.Model):
    student_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved_status = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.student.name} - {self.start_date} to {self.end_date}'