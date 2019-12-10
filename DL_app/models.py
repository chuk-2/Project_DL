from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class SimpleUser(AbstractUser):
    user_role = models.TextField()
    user_group = models.TextField()

    def __str__(self):
        return self.username


class User(models.Model):
    user_id = models.CharField(max_length=9999)
    user_password = models.TextField(default='123456')
    user_name = models.TextField()
    user_surname = models.TextField()
    user_date_of_birth = models.DateField('date of birth')
    user_role = models.TextField()


class News(models.Model):
    news_id = models.CharField(max_length=9999)
    news_author = models.TextField()
    news_title = models.TextField()
    news_content = models.TextField()
    news_date = models.DateTimeField('date')

    def datemonth(self):
        return self.news_date.strftime('%d %B')


class Course(models.Model):
    course_id = models.CharField(max_length=9999)
    course_name = models.TextField()
    course_teacher = models.TextField()


class TeacherCourses(models.Model):
    teacher_id = models.TextField()
    course_id = models.TextField()
