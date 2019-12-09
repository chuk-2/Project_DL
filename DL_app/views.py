from django.shortcuts import render
from .models import *
from django.http import HttpResponse


# Create your views here.
def main(request):
    all_news = News.objects.order_by('-news_date')
    return render(request, "DL_app/main.html", {'all_news': all_news})


def login(request):
    return render(request, "DL_app/login.html")


def student_user(request):
    all_course = Course.objects.order_by('-course_id')
    return render(request, "DL_app/courses.html", {'all_course': all_course})