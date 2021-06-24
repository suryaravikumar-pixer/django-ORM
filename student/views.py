
from django.shortcuts import render
from .models import Student
from django.db import connection #provides additional info in query like LIMIT, x - time 0.0015sec
from django.db.models import Q 
"""
Q   objects are helpfull for complex queries because they can be combined using 
    logical operators and(&), or(|), negation(~)
"""
# Part 2
def student_list_(request):

    posts = Student.objects.all()

    print(posts)
    print(posts.query)
    print(connection.queries)

    return render(request, 'output.html',{'posts':posts})

def student_list(request):

    # posts = Student.objects.filter(surname__startswith="S") | Student.objects.filter(surname__startswith="E")
    posts = Student.objects.filter(Q(surname__startswith='S') | ~Q(surname__startswith='j')) 
    """~Q Negation will give the oppose result of filter key word """
    

    print(posts)
    print(connection.queries)
    return render(request, "output.html", {'posts':posts})








# def student_list_(request):
#     posts = Student.objects.filter(surname__startswith='austin') | Student.objects.filter(surname__startswith='baldwin')

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})

# def student_list(request):
#     posts = Student.objects.filter(Q(surname__startswith='austin') | ~Q (surname__startswith='baldwin') | Q (surname__startswith='avery-parker'))

#     print(posts)
#     print(connection.queries)

#     return render(request, 'output.html',{'posts':posts})