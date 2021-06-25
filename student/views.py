
from django.shortcuts import render
from .models import Student, Teacher
from django.db import connection #provides additional info in query like LIMIT, x - time 0.0015sec
from django.db.models import Q 
"""
Q   objects are helpfull for complex queries because they can be combined using 

    logical operators and(&), or(|), negation(~)
"""

"""lt, lte, gt, gte operations performed and the Q methods"""
def student_list(request):
    """this will return records the not equal to the 12"""
    posts = Student.objects.filter(~Q(classroom=12)).only
    ('firstname', 'surname', 'age', )
    print(posts)
    print(connection.queries)
    return render(request, 'output.html', {'data':posts})






