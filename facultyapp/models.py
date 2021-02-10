from django.db import models

# Create your models here.

#hear i have created diffrent model model for diffrent department because i use normalization
#we can also create 1 table for all 
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

class Ce(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    #time=models.
    #uptime=models.TimeStamp()
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)


class Ec(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)

class It(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)

class Mh(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)

class Ch(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)

class Cl(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)

class Ic(models.Model):
    id=models.AutoField(primary_key=True)
    sem=models.IntegerField()
    uptime=models.DateTimeField(auto_now_add=True)
    userid=models.CharField(max_length=11)
    location=models.CharField(max_length=200)

class Reminder_student(models.Model):
    userid=models.CharField(max_length=11)
    date=models.DateField()
    reminder=models.CharField(max_length=500)
    sem=models.CharField(max_length=8)

class Reminder_faculty(models.Model):
    userid=models.CharField(max_length=11)
    date=models.DateField()
    reminder=models.CharField(max_length=500)



