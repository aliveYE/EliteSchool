from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    total_grade = models.IntegerField()
    status = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='students/', blank=True)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.grade.name} - {self.subject}"


class TestResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subject = models.CharField(max_length=100)
    score = models.IntegerField()
    max_score = models.IntegerField(default=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student.name} - {self.date}"