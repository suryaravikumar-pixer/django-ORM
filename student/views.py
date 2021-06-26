
from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection #provides additional info in query like LIMIT, x - time 0.0015sec
from django.db.models import Q 

"""
    Student.objects.all()--
        --objects is manager which provides interface between "database query opeatins and query model" 
        --all() collects all the data from student table
        --orm mapps the python object to the database fields
    one more thing we can use our native language python for query operations
"""


def student_list(request):
    """querying with raw function of SQL """
   
    # posts = Student.objects.all() 
    sql = "SELECT * FROM student_student"
    posts = Student.objects.raw(sql)
    """posts = Student.objects.all() 
    for string in Student.objects.raw("SELECT * FROM student_student"):
        print(string)"""

    print(posts)
    print(connection.queries) 
    return render(request, 'output.html', {'data':posts})






