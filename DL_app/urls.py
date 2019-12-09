from django.urls import path
from django.contrib.auth.views import auth_login
from . import views

app_name = "DL_app"

urlpatterns = [
    path('', views.main, name='main'),
    #path('/login/', views.login, name='login'),
    path('student_user/', views.student_user, name='student_user'),
    path('login', auth_login, name="login"),
]