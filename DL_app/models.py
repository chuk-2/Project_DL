from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=9999)
    user_name = models.TextField()
    user_surname = models.TextField()
    user_date_of_birth = models.DateField('date of birth')


class News(models.Model):
    news_id = models.CharField(max_length=9999)
    news_author = models.TextField()
    news_title = models.TextField()
    news_content = models.TextField()
    news_date = models.DateTimeField('date')
