# Generated by Django 3.1.5 on 2021-02-26 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0002_student_coment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='coment',
        ),
    ]
