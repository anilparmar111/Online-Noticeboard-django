# Generated by Django 3.0.3 on 2020-02-25 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_ce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=7)),
                ('bdate', models.DateField()),
                ('branch', models.CharField(max_length=4)),
                ('mno', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
