from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import HttpResponse


# Create your views here.
def main(request):
    all_news = News.objects.order_by('-news_date')
    return render(request, "DL_app/main.html", {'all_news': all_news})


def login(request):
    return render(request, "DL_app/login.html")


def courses(request):
    all_course = Course.objects.order_by('-course_id')
    return render(request, "DL_app/courses.html", {'all_course': all_course})


def student_attendance(request, course_id):
    course_art = get_object_or_404(Course, pk=course_id)
    return render(request, "DL_app/attendance_student.html", {"course": course_art})


def student_scores(request, course_id):
    course_art = get_object_or_404(Course, pk=course_id)
    return render(request, "DL_app/score_student.html", {"course": course_art})
