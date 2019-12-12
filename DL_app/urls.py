from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import auth_login
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = "DL_app"

urlpatterns = [
    path('', views.main, name='main'),
    path('courses/', views.courses, name='courses'),
    path('student_attendance/<int:course_id>/', views.student_attendance, name='student_attendance'),
    path('student_scores/<int:course_id>/', views.student_scores, name='student_scores'),
    path('course_user/<int:course_id>/', views.course_user, name='course_user'),
    path('task_user/<int:task_id>/', views.task_user, name='task_user'),
    path('login', auth_login, name="login"),
    url(r'^media/(?P<path>.*)$', views.download),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()