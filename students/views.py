from django.shortcuts import render
from .models import Student


def student_list(request):
    first_name = request.GET.get('first_name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    date_of_birth = request.GET.get('date_of_birth')
    gender = request.GET.get('gender')
    address = request.GET.get('address')
    if first_name and last_name and email and date_of_birth and gender and address:
        Student.objects.create(
            first_name = first_name,
            last_name = last_name,
            email = email,
            date_of_birth = date_of_birth,
            gender = gender,
            address = address
        )
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)