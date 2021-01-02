# Generated by Django 3.0.3 on 2020-02-26 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminloginapp', '0002_student_ch_student_cl_student_ec_student_ic_student_it_student_mh'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_ce',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ce',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ch',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ch',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_cl',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_cl',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ec',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ec',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ic',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_ic',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_it',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_it',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_mh',
            name='password',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AddField(
            model_name='student_mh',
            name='userid',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='student_ce',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_ce',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ce',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_ce',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ce',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student_ch',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_ch',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ch',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_ch',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ch',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student_cl',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_cl',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_cl',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_cl',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_cl',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student_ec',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_ec',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ec',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_ec',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ec',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student_ic',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_ic',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ic',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_ic',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_ic',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student_it',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_it',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_it',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_it',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_it',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AlterField(
            model_name='student_mh',
            name='branch',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='student_mh',
            name='fname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_mh',
            name='gender',
            field=models.CharField(default='', max_length=7),
        ),
        migrations.AlterField(
            model_name='student_mh',
            name='lname',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='student_mh',
            name='mno',
            field=models.CharField(default='', max_length=12),
        ),
    ]