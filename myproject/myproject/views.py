from datetime import datetime
from typing import List
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  isActive = True
  if request.method == 'POST':
    check = request.POST.get('check')
    print(check)
    if check is None:
      isActive = False
  date = datetime.now()
  name = "Learning Django"
  list_of_programs = [
    'WAP to check even or odd',
    'WAP to check prime number'
  ]
  student ={
    'student_name': "Rahul",
    'student_college':'XYZ',
    'student_city':'GOA'

  }

  data = {
    'date': date,
    'isActive': isActive,
    'name':name,
    'list_of_programs' : list_of_programs,
    'student_data': student
  }
  return render(request,"home.html",data)

def about(request):
  return render(request,"about.html",{})

def services(request):
  return render(request,"services.html",{})