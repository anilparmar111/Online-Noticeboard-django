from django.contrib.messages.storage import default_storage
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import random
import os
from facultyapp.models import Reminder_student
from django.db import connection
from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf, request
from django.contrib import auth
from django.views.generic import TemplateView
from adminloginapp.models import Faculty_ce
from adminloginapp.models import Faculty_ec
from adminloginapp.models import Faculty_it
from adminloginapp.models import Faculty_mh
from adminloginapp.models import Faculty_ic
from adminloginapp.models import Faculty_ch
from adminloginapp.models import Faculty_cl
from facultyapp.models import Ce
from facultyapp.models import Ec
from facultyapp.models import It
from facultyapp.models import Ch
from facultyapp.models import Mh
from facultyapp.models import Cl
from facultyapp.models import Ic
from adminloginapp.models import Student_ce
from adminloginapp.models import Student_ec
from adminloginapp.models import Student_it
from adminloginapp.models import Student_mh
from adminloginapp.models import Student_ic
from adminloginapp.models import Student_ch
from adminloginapp.models import Student_cl
from studentapp.models import Ce_reminder
from studentapp.models import Ec_reminder
from studentapp.models import It_reminder
from studentapp.models import Mh_reminder
from studentapp.models import Ch_reminder
from studentapp.models import Cl_reminder
from studentapp.models import Ic_reminder
import datetime
from datetime import date
import socket
socket.getaddrinfo('localhost', 8080)
#from .models import UploadMetirial_CE
#from .forms import UploadFile

# Create your views here.


def course(request):
    userid=request.session['id']
    branch=request.session['branch']
    csem=request.session['csem']
    if(branch == "CE"):
        for row in Student_ce.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in Ce.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                #send_mail("notice have been uploaded","this is actual mail","apnoticeboard@gmail.com",['anilparmar76983@gmail.com'],fail_silently=False)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")
    elif(branch == "EC"):
        for row in Student_ec.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in Ec.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")
    


    elif(branch == "IT"):
        for row in Student_it.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in It.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")
    
    elif(branch == "MH"):
        for row in Student_mh.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in Mh.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")
        
    elif(branch == "CH"):
        for row in Student_ch.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in Ch.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")
    


    elif(branch == "CL"):
        for row in Student_cl.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in Cl.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")


    elif(branch == "IC"):
        for row in Student_ic.objects.all():
            if(userid == row.userid): 
                notices = {}
                i = 1
                for data in Ic.objects.filter(sem=csem).order_by('-id'):
                    file = open(data.location, "r")
                    filedata = file.readlines()
                    file.close()
                    notices[i] = {
                        "name": row.fname+" "+row.mname+" "+row.lname,
                        "uptime": str(data.uptime.date()),
                        "notice": filedata
                    }
                    i = i+1
                print(notices)
                return render(None,'studentapp/course.html',{'c':notices})
                #return HttpResponseRedirect("/student/home")
    

    #return render(None, 'studentapp/course.html')


def login(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'studentapp/login.html', c)


def auth(request):
    c = {}
    c.update(csrf(request))
    userid = request.POST.get('username')
    if(len(userid) < 10):
        return render(None, 'studentapp/login.html', c)
    branch = userid[2:4]
    password = request.POST.get('password')
    if(branch == "CE"):
        for row in Student_ce.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in Ce_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)

    elif(branch == "EC"):
        for row in Student_ec.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in Ec_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)

    elif(branch == "IT"):
        for row in Student_it.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in It_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)

    elif(branch == "MH"):
        for row in Student_mh.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in Mh_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)

    elif(branch == "CH"):
        for row in Student_ch.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in Ch_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)

    elif(branch == "CL"):
        for row in Student_cl.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in Cl_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)

    elif(branch == "IC"):
        for row in Student_ic.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['id'] = userid
                request.session['branch']=branch
                today = date.today()
                for reminder in Ic_reminder.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        #print("this should be delete")
                        reminder.delete()
                for reminder in Reminder_student.objects.all():
                    rdate = reminder.date
                    if rdate < today:
                        reminder.delete()
                reg = row.regtime.date()
                today = date.today()
                day = (today-reg).days
                csem = ((int(day/180))+1)
                request.session['csem'] = csem
                return HttpResponseRedirect("/student/home")
        else:
            return render(None, 'studentapp/login.html', c)
    else:
        return render(None, 'studentapp/login.html', c)


def home(request):
    userid = request.session['id']
    today = date.today()
    counts = 0
    for reminder in Ce_reminder.objects.filter(userid=userid):  
        counts = counts+1
    countf = 0
    csem = request.session['csem']
    for reminder in Reminder_student.objects.all():
        semester = reminder.sem
        for word in semester:
            if word.isdigit():
                if(str(word) == str(csem)):
                    countf = countf+1
    total = countf+counts
    return render(request, "studentapp/studenthome.html", {'counts': counts, 'countf': countf, 'total': total})


def set_reminder(request):
    return render(request, "studentapp/setreminder.html")


def setreminder(request):
    reminder = request.POST.get('reminder')
    date = request.POST.get('rdate')
    id = ''
    if 'id' in request.session:
        id = request.session['id']
    else:
        return render(None, "studentapp/login.html")
    if(request.session['branch']=="CE"):
        obj = Ce_reminder()
    elif(request.session['branch']=="EC"):
        obj = Ec_reminder()
    elif(request.session['branch']=="IT"):
        obj = It_reminder()
    elif(request.session['branch']=="MH"):
        obj = Mh_reminder()
    elif(request.session['branch']=="CH"):
        obj = Ch_reminder()
    elif(request.session['branch']=="CL"):
        obj = Cl_reminder()
    elif(request.session['branch']=="IC"):
        obj = Ic_reminder()
    obj.userid = id
    obj.reminder = reminder
    obj.date = date
    obj.save()
    #return HttpResponse("reminder is set")
    return render(None,"studentapp/studenthome.html",{"msg":"Reminder Set Succesfully"})


def show_student_reminder(request):
    reminders = {}
    i = 0
    userid = request.session['id']
    if(request.session['branch']=="CE"): 
        for reminderobj in Ce_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1

    elif(request.session['branch']=="EC"): 
        for reminderobj in Ec_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1
    elif(request.session['branch']=="IT"): 
        for reminderobj in It_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1
    elif(request.session['branch']=="MH"): 
        for reminderobj in Mh_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1
    elif(request.session['branch']=="CH"): 
        for reminderobj in Ch_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1
    elif(request.session['branch']=="CL"): 
        for reminderobj in Cl_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1
    elif(request.session['branch']=="IC"): 
        for reminderobj in Ic_reminder.objects.filter(userid=userid):
            reminders[i] = {
                "reminder": reminderobj.reminder,
                "date": reminderobj.date
            }
            i = i+1
    
    return render(None, "studentapp/showreminder.html", {"reminders": reminders})


def show_faculty_reminder(request):
    reminders = {}
    i = 0
    userid = request.session['id']
    csem = request.session['csem']
    for reminderobj in Reminder_student.objects.all():
        semester = reminderobj.sem
        for word in semester:
            if word.isdigit():
                if(str(word) == str(csem)):
                    fid = reminderobj.userid
                    fname = ""
                    if(request.session['branch']=="CE"):
                        for facultyobj in Faculty_ce.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    elif(request.session['branch']=="EC"):
                        for facultyobj in Faculty_ec.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    elif(request.session['branch']=="IT"):
                        for facultyobj in Faculty_it.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    elif(request.session['branch']=="MH"):
                        for facultyobj in Faculty_mh.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    elif(request.session['branch']=="CH"):
                        for facultyobj in Faculty_ch.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    elif(request.session['branch']=="CL"):
                        for facultyobj in Faculty_cl.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    elif(request.session['branch']=="IC"):
                        for facultyobj in Faculty_ic.objects.filter(userid=fid):
                            fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
                    

                    reminders[i] = {
                        "reminder": reminderobj.reminder,
                        "date": reminderobj.date,
                        "fname": fname
                    }
                    i = i+1
    return render(None, "studentapp/showreminder_faculty.html", {"reminders": reminders})


def upload_data(request):
    c = {}
    c.update(csrf(request))
    return render(None, "studentapp/upload_data.html", c)


def email_request(request):
    userid = request.session['id']
    if(request.session['branch']=="CE"):
        for studentobj in Student_ce.objects.filter(userid=userid):
            studentobj.email_request="1"
    elif(request.session['branch']=="EC"):
        for studentobj in Student_ec.objects.filter(userid=userid):
            studentobj.email_request="1"
    elif(request.session['branch']=="IT"):
        for studentobj in Student_it.objects.filter(userid=userid):
            studentobj.email_request="1"
    elif(request.session['branch']=="MH"):
        for studentobj in Student_mh.objects.filter(userid=userid):
            studentobj.email_request="1"
    elif(request.session['branch']=="CH"):
        for studentobj in Student_ch.objects.filter(userid=userid):
            studentobj.email_request="1"
    elif(request.session['branch']=="CL"):
        for studentobj in Student_cl.objects.filter(userid=userid):
            studentobj.email_request="1"
    elif(request.session['branch']=="IC"):
        for studentobj in Student_ic.objects.filter(userid=userid):
            studentobj.email_request="1"
    return render(None,"studentapp/studenthome.html",{"msg":"Now You can get email when new notice is uploded"})

def logout(request):
    del request.session['id']
    del request.session['csem']
    del request.session['branch']
    return render(None,"studentapp/login.html",{"msg":"Logout Sucessfully"})