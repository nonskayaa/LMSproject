from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/indexForNotAuthorized.html')


def profile(request):
    return render(request, 'main/profile.html')


def authorizedMain(request):
    return render(request, 'main/authorizedMainPage.html')

def myCourses(request):
    return render(request, 'main/myCourses.html')