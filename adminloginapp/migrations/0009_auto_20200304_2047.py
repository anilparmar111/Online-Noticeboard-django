# Generated by Django 3.0.3 on 2020-03-04 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminloginapp', '0008_ch_cl_ec_ic_it_mh'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ce',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ch',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cl',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ec',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='ic',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='it',
            name='sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='mh',
            name='sem',
            field=models.IntegerField(),
        ),
    ]
