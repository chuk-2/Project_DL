# Generated by Django 2.2.6 on 2019-12-12 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DL_app', '0014_schedule_tasks_userschedule_usertask'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='task_id',
            field=models.CharField(default=1, max_length=9999),
            preserve_default=False,
        ),
    ]
