
from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection #provides additional info in query like LIMIT, x - time 0.0015sec
from django.db.models import Q 
"""
Q   objects are helpfull for complex queries because they can be combined using 

    logical operators and(&), or(|), negation(~)
"""

"""Union operation returns the all the records after eleminating the duplicates"""
def student_list(request):
    posts = Student.objects.all().values_list("firstname").union(
        Teacher.objects.all().values_list("firstname"))
    
    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'posts':posts})






