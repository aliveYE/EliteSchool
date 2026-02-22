from django.shortcuts import render

students_demo = [
    {
        "id": 1,
        "name": "Ahmed Al-Salem",
        "gender": "Male",
        "dob": "2014-05-12",
        "status": "Excellent",
        "grade": 98,
        "grade_level": 4,
        "attendance": 180,
        "total_days": 190,
        "photo": "students/1.jpg"
    },
    {
        "id": 2,
        "name": "Sara Mahmoud",
        "gender": "Female",
        "dob": "2014-08-21",
        "status": "Very Good",
        "grade": 91,
        "grade_level": 4,
        "attendance": 170,
        "total_days": 190,
        "photo": "students/2.jpg"
    },
]

def loader(request):
    return render(request, 'loader.html')

def home(request):
    return render(request, 'home.html')

def lessons(request):
    return render(request, 'lessons.html')

def students(request):
    grade = int(request.GET.get('grade', 4))
    filtered = [s for s in students_demo if s['grade_level'] == grade]
    sorted_students = sorted(filtered, key=lambda x: x['grade'], reverse=True)
    return render(request, 'students.html', {
        'students': sorted_students,
        'current_grade': grade
    })
    
    
def student_profile(request, pk):
    student = next(s for s in students_demo if s['id'] == pk)
    student['attendance_percent'] = round(
        (student['attendance'] / student['total_days']) * 100, 1
    )
    return render(request, 'student_profile.html', {'student': student})
    


def grade_dashboard(request):
    return render(request, 'grade_dashboard.html')

def add_student(request):
    return render(request, 'add_student.html')