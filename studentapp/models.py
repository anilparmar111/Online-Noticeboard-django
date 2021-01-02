from django.db import models

# Create your models here.


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
