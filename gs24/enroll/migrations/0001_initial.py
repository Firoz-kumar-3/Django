# Generated by Django 3.1.5 on 2021-02-26 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField()),
                ('stuname', models.CharField(max_length=63)),
                ('stumail', models.EmailField(max_length=60)),
                ('stupass', models.CharField(max_length=68)),
            ],
        ),
    ]
