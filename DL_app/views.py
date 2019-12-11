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
    username = request.user.username
    user_role = ''
    user_group = ''
    user_id = ''
    group_id = ''
    i = 0
    query = 'SELECT * FROM DL_app_Course'
    for user in SimpleUser.objects.raw('SELECT * FROM DL_app_SimpleUser WHERE username=%s', [username]):
        user_role = user.user_role
    if user_role == "Student":
        for user in SimpleUser.objects.raw('SELECT * FROM DL_app_SimpleUser WHERE username=%s', [username]):
            user_group = user.user_group
        for group in Group.objects.raw('SELECT * FROM DL_app_Group WHERE group_name=%s', [user_group]):
            group_id = group.group_id
        for groupcourse in GroupCourse.objects.raw('SELECT * FROM DL_app_GroupCourse WHERE group_id=%s', [group_id]):
            if i == 0:
                query = query + ' WHERE'
                query = query + ' course_id=' + groupcourse.course_id
            else:
                query = query + ' OR course_id=' + groupcourse.course_id
            i = i + 1
    elif user_role == "Teacher":
        for user in SimpleUser.objects.raw('SELECT * FROM DL_app_SimpleUser WHERE username=%s', [username]):
            user_id = user.id
        for groupcourse in TeacherCourses.objects.raw('SELECT * FROM DL_app_TeacherCourses WHERE teacher_id=%s', [user_id]):
            if i == 0:
                query = query + ' WHERE'
                query = query + ' course_id=' + groupcourse.course_id
            else:
                query = query + ' OR course_id=' + groupcourse.course_id
            i = i + 1
    all_course = Course.objects.raw(query)
    print(query)
    #all_course = Course.objects.filter(course_id=1).order_by('-course_id')
    #if query:
    #    all_course = all_course.filter(pk=query)
    return render(request, "DL_app/courses.html", {'all_course': all_course})


def student_attendance(request, course_id):
    course_art = get_object_or_404(Course, pk=course_id)
    return render(request, "DL_app/attendance_student.html", {"course": course_art})


def student_scores(request, course_id):
    course_art = get_object_or_404(Course, pk=course_id)
    return render(request, "DL_app/score_student.html", {"course": course_art})
