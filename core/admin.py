from django.contrib import admin
from .models import Grade, Student, Lesson, TestResult, Attendance

admin.site.register(Grade)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(TestResult)
admin.site.register(Attendance)