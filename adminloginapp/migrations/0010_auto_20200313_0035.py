# Generated by Django 3.0.3 on 2020-03-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminloginapp', '0009_auto_20200304_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty_ce',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='faculty_ch',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='faculty_cl',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='faculty_ec',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='faculty_ic',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='faculty_it',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='faculty_mh',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_ce',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_ch',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_cl',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_ec',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_ic',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_it',
            name='branch',
        ),
        migrations.RemoveField(
            model_name='student_mh',
            name='branch',
        ),
        migrations.AddField(
            model_name='faculty_ce',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty_ch',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty_cl',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty_ec',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty_ic',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty_it',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='faculty_mh',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_ce',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_ch',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_cl',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_ec',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_ic',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_it',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='student_mh',
            name='mname',
            field=models.CharField(default='', max_length=20),
        ),
    ]
