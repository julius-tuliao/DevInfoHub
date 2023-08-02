from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {
        'id': 1,
        'title': 'E-commerce Website',
        'description': 'Develop an online platform for buying and selling products. Implement features such as user authentication, product catalog, shopping cart, and secure payment processing.',
    },
    {
        'id': 2,
        'title': 'Social Media Application',
        'description': 'Build a social media platform that allows users to create profiles, connect with friends, post updates, share multimedia content, and engage in discussions.',
    },
    {
        'id': 3,
        'title': 'Task Management System',
        'description': 'Create a web application for managing tasks, deadlines, and projects. Users should be able to assign tasks, track progress, and receive notifications.',
    },
    {
        'id': 4,
        'title': 'Fitness Tracking Mobile App',
        'description': 'Design a mobile app that enables users to track their fitness activities, set fitness goals, and view progress through interactive charts and personalized recommendations.',
    },
    {
        'id': 5,
        'title': 'Online Learning Platform',
        'description': 'Develop a comprehensive online learning platform with courses, quizzes, and interactive lessons. Include features for progress tracking and instructor-student communication.',
    },
]


def projects(request):
    page = 'projects'
    number = 10 
    
    context = {'page':page , 'number':10, 'projects': projectsList}
    return render(request,'projects/projects.html', context)

def project(request,pk):
    projectObj = None

    for project in projectsList:

        if(project["id"] == int(pk)):

            projectObj = project 
  

    return render(request,"projects/single-project.html", {'project': projectObj})