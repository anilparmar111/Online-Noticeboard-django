# Generated by Django 3.0.3 on 2020-03-15 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultyapp', '0002_auto_20200314_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ce',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ch',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cl',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ec',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ic',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='it',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mh',
            name='uptime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
