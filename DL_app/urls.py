from django.urls import path
from django.contrib.auth.views import auth_login
from . import views

app_name = "DL_app"

urlpatterns = [
    path('', views.main, name='main'),
    path('courses/', views.courses, name='courses'),
    path('student_attendance/<int:course_id>/', views.student_attendance, name='student_attendance'),
    path('student_scores/<int:course_id>/', views.student_scores, name='student_scores'),
    path('login', auth_login, name="login"),
]