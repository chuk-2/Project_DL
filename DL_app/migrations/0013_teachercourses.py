# Generated by Django 2.2.6 on 2019-12-11 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DL_app', '0012_delete_teachercourses'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.TextField()),
                ('course_id', models.TextField()),
            ],
        ),
    ]
