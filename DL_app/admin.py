from django.contrib import admin

from .models import User, News, Course, TeacherCourses, SimpleUser


# Register your models here.
admin.site.register(User)
admin.site.register(News)
admin.site.register(Course)
admin.site.register(TeacherCourses)
admin.site.register(SimpleUser)
