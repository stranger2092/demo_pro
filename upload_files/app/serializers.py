from rest_framework import serializers
from .models import Student, Teacher, LeaveForm

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class LeaveFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveForm
        fields = '__all__'