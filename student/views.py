
from django.shortcuts import render
from .models import Student
from django.db import connection #provides additional info in query like LIMIT, x - time 0.0015sec
from django.db.models import Q 
"""
Q   objects are helpfull for complex queries because they can be combined using 

    logical operators and(&), or(|), negation(~)
"""

def student_list(request):
    posts = Student.objects.filter(Q(surname__startswith='E') & Q(firstname__startswith='N')) 
    print(posts)
    return render(request, 'output.html', {'posts':posts})






