from django.contrib import admin

from .models import News, Course, TeacherCourses, SimpleUser, Group, GroupCourse


# Register your models here.
admin.site.register(News)
admin.site.register(Course)
admin.site.register(TeacherCourses)
admin.site.register(SimpleUser)
admin.site.register(Group)
admin.site.register(GroupCourse)
