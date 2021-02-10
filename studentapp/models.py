from django.db import models

# Create your models here.

#hear i have created diffrent model model for diffrent department because i use normalization
#we can also create 1 table for all table like this 
# class faculty(models.model):
#     id
#     sem
#     uptime
#     userid
#     location
#     branch // for diffrent branch's faculty
#     but if we thousands of data then in this table
#     we have redundant data in branch column 
#     so i use difrent diffrent database table for diffrent diffrent branch
#     otherwise i can create 1 table for all the facultys
#     If You have any suggestion then please give mi

class Ce_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()


class Ec_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()


class It_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()


class Mh_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()


class Cl_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()


class Ch_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()


class Ic_reminder(models.Model):
    userid = models.CharField(max_length=11)
    reminder = models.CharField(max_length=200)
    date = models.DateField()
