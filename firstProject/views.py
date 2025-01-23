from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    data = {
        'name': 'John Doe',
        'age': 30,
        'jobTitle': 'Software Engineer',
        'skills': ['Python', 'Django', 'JavaScript', 'React'],
        'experience': [
            {
                'title': 'Software Engineer',
                'company': 'ABC Inc',
                'years': 3
            },
            {
                'title': 'Software Engineer',
                'company': 'XYZ Inc',
                'years': 2
            }
        ]
    }
    return render(request, 'index.html', data)

def aboutUs(request):
    return HttpResponse("About Us Page")

def contactUs(request):
    return HttpResponse("Contact Us Page")

def jobs(request):
    return HttpResponse("Jobs Page")

def jobDetails(request, jobId):
    return HttpResponse("Job Details Page: " + str(jobId))