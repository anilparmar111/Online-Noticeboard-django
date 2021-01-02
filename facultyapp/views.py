from django.core.mail import send_mail
from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf, request
from django.contrib import auth
from django.views.generic import TemplateView
import datetime
from datetime import date
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
import os
import socket
socket.getaddrinfo('localhost', 8080)
from .models import Reminder_student
from .models import Reminder_faculty
# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'facultyapp/login.html', c)


"""def validation(request):
    #obj=Faculty_ce.objects.get()
    '''print ("hello")
    userid=request.POST.get('fid')
    password=request.POST.get('fpswd')
    for row in Faculty_ce.objects.all(): 
        userid=row.userid
        password=row.password
        print(userid+password)
    return HttpResponseRedirect("hello")'''
    branch=request.POST.get('fbranch')
    userid=request.POST.get('fid')
    password=request.POST.get('fpswd')
    #userid=row.userid
    #password=row.password
    c = {}
    c.update(csrf(request))
    if(branch=="ce"):
        for row in Faculty_ce.objects.all():
            if(userid==row.userid and password==row.password):
                request.session['userid']=userid
                request.session['branch']=branch
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)

    elif(branch=="ec"):
        for row in Faculty_ec.objects.all():
            if(userid==row.userid and password==row.password):
                request.session['userid']=userid
                request.session['branch']=branch
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)

    elif(branch=="it"):
        for row in Faculty_it.objects.all():
            if(userid==row.userid and password==row.password):
                request.session['userid']=userid
                request.session['branch']=branch
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)

    elif(branch=="mh"):
        for row in Faculty_mh.objects.all():
            if(userid==row.userid and password==row.password):
                request.session['userid']=userid
                request.session['branch']=branch
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)

    elif(branch=="ch"):
        for row in Faculty_ch.objects.all():
            request.session['userid']=userid
            request.session['branch']=branch
            if(userid==row.userid and password==row.password):
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)

    elif(branch=="cl"):
        for row in Faculty_cl.objects.all():
            if(userid==row.userid and password==row.password):
                request.session['userid']=userid
                request.session['branch']=branch
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)


    elif(branch=="ic"):
        for row in Faculty_ic.objects.all():
            if(userid==row.userid and password==row.password):
                request.session['userid']=userid
                request.session['branch']=branch
                return render(None,'facultyapp/upload_notice.html',c)
        else:
            return render(None,'facultyapp/login.html',c)
    else:
        return render(None,'facultyapp/login.html',c)"""


def validation(request):
    c = {}
    c.update(csrf(request))
    userid = request.POST.get('username')
    if(len(userid) < 10):
        return render(None, 'facultyapp/login.html', c)
    branch = userid[2:4]
    password = request.POST.get('password')
    # print(branch)
    # return render(None,'facultyapp/upload_notice.html',c)
    if(branch == "CE"):
        for row in Faculty_ce.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['userid'] = userid
                request.session['branch'] = branch
                return render(None, 'facultyapp/facultyhome.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)

    elif(branch == "EC"):
        for row in Faculty_ec.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['userid'] = userid
                request.session['branch'] = branch
                return render(None, 'facultyapp/upload_notice.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)

    elif(branch == "IT"):
        for row in Faculty_it.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['userid'] = userid
                request.session['branch'] = branch
                return render(None, 'facultyapp/upload_notice.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)

    elif(branch == "MH"):
        for row in Faculty_mh.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['userid'] = userid
                request.session['branch'] = branch
                return render(None, 'facultyapp/upload_notice.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)

    elif(branch == "CH"):
        for row in Faculty_ch.objects.all():
            request.session['userid'] = userid
            request.session['branch'] = branch
            if(userid == row.userid and password == row.password):
                return render(None, 'facultyapp/upload_notice.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)

    elif(branch == "CL"):
        for row in Faculty_cl.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['userid'] = userid
                request.session['branch'] = branch
                return render(None, 'facultyapp/upload_notice.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)

    elif(branch == "IC"):
        for row in Faculty_ic.objects.all():
            if(userid == row.userid and password == row.password):
                request.session['userid'] = userid
                request.session['branch'] = branch
                return render(None, 'facultyapp/upload_notice.html', c)
        else:
            return render(None, 'facultyapp/login.html', c)
    else:
        return render(None, 'facultyapp/login.html', c)


def upload(request):
    branch = request.session['branch']
    if not os.path.exists(branch):
        os.makedirs(branch)

    dpath = os.getcwd()
    dpath = dpath+"\\"+branch
    if(branch == "CE"):
        if((Ce.objects.order_by('-id')).exists()):
            idobj = Ce.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = Ce()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_ce.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})
    elif(branch == "EC"):
        if((Ec.objects.order_by('-id')).exists()):
            idobj = Ec.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = Ec()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_ec.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})

        #return render(None, 'facultyapp/succes.html')
    elif(branch == "IT"):
        if((It.objects.order_by('-id')).exists()):
            idobj = It.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = It()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_it.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})

        #return render(None, 'facultyapp/succes.html')
    elif(branch == "MH"):
        if((Mh.objects.order_by('-id')).exists()):
            idobj = Mh.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = Mh()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_mh.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})

        #return render(None, 'facultyapp/succes.html')
    elif(branch == "CH"):
        if((Ch.objects.order_by('-id')).exists()):
            idobj = Ch.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = Ch()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_ch.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})

        #return render(None, 'facultyapp/succes.html')
    elif(branch == "CL"):
        if((Cl.objects.order_by('-id')).exists()):
            idobj = Cl.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = Cl()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_cl.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})

        #return render(None, 'facultyapp/succes.html')
    elif(branch == "IC"):
        if((Ic.objects.order_by('-id')).exists()):
            idobj = Ic.objects.order_by('-id')[0]
            lid = int(idobj.id)+1
        else:
            lid = 1
        text = request.POST.get('notice')
        fnm = str(lid)+".txt"
        filepath = dpath+"\\"+fnm
        file1 = open(filepath, "w+")
        file1.writelines(text)
        file1.close()
        for sem in request.POST.getlist('sem[]'):
            obj = Ic()
            obj.sem = sem
            obj.location = filepath
            obj.userid = request.session['userid']
            obj.save()
        for student in Student_ic.objects.all():
            reg = student.regtime.date()
            today = date.today()
            day = (today-reg).days
            csem = ((int(day/180))+1)
            for sem in request.POST.getlist('sem[]'):
                if(csem==sem and student.email_request=="1"):
                    print ("====> Notification email is send if you uncomment below line")
                    #send_mail("sem "+str(csem),student.fname,"apnoticeboard@gmail.com",[student.email],fail_silently=False)
        return render(None, 'facultyapp/facultyhome.html',{"msg":"Notice Uploaded Succesfully"})

        #return render(None, 'facultyapp/succes.html')

def home(request):
    return render(request,"facultyapp/facultyhome.html")


def reminder_set_student(request):
    c = {}
    c.update(csrf(request))
    return render(None,"facultyapp/setreminder.html",c)



def addreminder_data(request):
    print(request.POST.getlist('sem[]'))
    semester=""
    for sem in request.POST.getlist('sem[]'):
        #print("sem is :",sem)
        #obj = Ce()
        #obj.sem = sem
        #obj.location = filepath
        #obj.userid = request.session['userid']
        #obj.save()
        #print(sem)
        semester=semester+sem
    obj=Reminder_student()
    obj.sem=semester
    obj.date=request.POST.get('date')
    obj.reminder=request.POST.get('reminder')
    obj.userid=request.session['userid']
    obj.save()
    return render(None,"facultyapp/facultyhome.html",{"msg":"Reminder Set Succesfully"})

    #return HttpResponse("reminder is set")
    


def upload_notice(request):
    c = {}
    c.update(csrf(request))
    return render(None,"facultyapp/upload_notice.html",c)

def set_self_reminder(request):
    c = {}
    c.update(csrf(request))
    return render(None,"facultyapp/set_self_reminder.html",c)

def add_self_reminder_data(request):
    obj=Reminder_faculty()
    #obj.sem=semester
    obj.date=request.POST.get('date')
    obj.reminder=request.POST.get('reminder')
    obj.userid=request.session['userid']
    obj.save()
    return render(None,"facultyapp/facultyhome.html",{"msg":"Reminder Set Succesfully"})


def show_self_reminder(request):
    reminders = {}
    i = 0
    userid = request.session['userid']
    #csem = request.session['csem']
    for reminderobj in Reminder_faculty.objects.all():
        fid = reminderobj.userid
        for facultyobj in Faculty_ce.objects.filter(userid=fid):
                
                reminders[i] = {
                    "reminder": reminderobj.reminder,
                    "date": reminderobj.date,
                }
                i = i+1
        #semester = reminderobj.sem
        # for word in semester:
        #     if word.isdigit():
        #         if(str(word) == str(csem)):
        #             fid = reminderobj.userid
        #             fname = ""
        #             for facultyobj in Faculty_ce.objects.filter(userid=fid):
        #                 fname = facultyobj.fname+" "+facultyobj.mname+" "+facultyobj.lname
        #             reminders[i] = {
        #                 "reminder": reminderobj.reminder,
        #                 "date": reminderobj.date,
        #                 "fname": fname
        #             }
        #             i = i+1
    return render(None, "studentapp/showreminder_faculty.html", {"reminders": reminders})

