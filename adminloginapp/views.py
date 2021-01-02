from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib import auth
from django.views.generic import TemplateView
import datetime
from datetime import date
from adminloginapp.models import Student_ce
from adminloginapp.models import Student_ec
from adminloginapp.models import Student_it
from adminloginapp.models import Student_mh
from adminloginapp.models import Student_ic
from adminloginapp.models import Student_ch
from adminloginapp.models import Student_cl
from adminloginapp.models import Faculty_ce
from adminloginapp.models import Faculty_ec
from adminloginapp.models import Faculty_it
from adminloginapp.models import Faculty_mh
from adminloginapp.models import Faculty_ic
from adminloginapp.models import Faculty_ch
from adminloginapp.models import Faculty_cl

# Create your views here.


def login(request):
    c = {}
    c.update(csrf(request))
    return render(None, 'adminloginapp/login.html',c)

"""def auth_view(request):
    username = request.POST.get('uname', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username="admin", password="password") 
    if user is not None:
        request.session['user']="admin"
	    auth.login(request, user)
        #request.session['user']='admin'
	    return HttpResponseRedirect('/adminlogin/signup/')
    else:
        c ={}
        c.update(csrf(request))
        return HttpResponseRedirect("/adminlogin/invalidlogin/")
    #if user is not None:"""
def auth_view(request):
    username=request.POST.get('uname','')
    password=request.POST.get('password','')
    user=auth.authenticate(username="admin",password="admin")
    if (user is not None and username=="admin" and password=="admin"):
        request.session['user']="admin"
        auth.login(request,user)
        return HttpResponseRedirect('/adminlogin/signup/')
    else:
        c={}
        c.update(csrf(request))
        #return render(None,"adminloginapp/login.html")
        return HttpResponseRedirect('/adminlogin/invalidlogin/')
	

def signup(request):
    c = {}
    c.update(csrf(request))
    if 'user' not in request.session:
        return render(None, 'adminloginapp/login.html',c)
    
    return render(None, "adminloginapp/signup.html", c)

def invalidlogin(request):
    #c = {}
    #c.update(csrf(request))
    #if 'user' not in request.session:
        #return render(None, 'adminloginapp/login.html',{'c':"invalid user id"})
    return render(None, "adminloginapp/invalid.html")

#def insertstudent(request):   
    branch = request.POST.get('branch', '')
    date = request.POST.get('bdate', '')
    length = len(date)
    passw = ""
    month = ""
    dat = ""
    year = ""
    for i in range(0, 4):
        year += date[i]
    for i in range(5, 7):
        month += date[i]
    for i in range(8, 10):
        dat += date[i]
    passw = dat+"/"+month+"/"+year
    
    if(branch == "CE"): 
        if((Student_ce.objects.order_by('-id')).exists()):
            idobj=Student_ce.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4) 
        data = Student_ce()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')
    elif(branch == "EC"):
        #idobj = Student_ec.objects.order_by('-id')[0]
        if((Student_ec.objects.order_by('-id')).exists()):
            idobj=Student_ec.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4)
        data = Student_ec()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "IT"):
        #idobj = Student_it.objects.order_by('-id')[0]
        if((Student_it.objects.order_by('-id')).exists()):
            idobj=Student_it.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4)
        data = Student_it()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "MH"):
        #idobj = Student_mh.objects.order_by('-id')[0]
        if((Student_mh.objects.order_by('-id')).exists()):
            idobj=Student_mh.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4)
        data = Student_mh()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "CH"):
        #idobj = Student_ch.objects.order_by('-id')[0]
        if((Student_ch.objects.order_by('-id')).exists()):
            idobj=Student_ch.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4)
        data = Student_ch()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "IC"):
        #idobj = Student_ic.objects.order_by('-id')[0]
        if((Student_ic.objects.order_by('-id')).exists()):
            idobj=Student_ic.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4)
        data = Student_ic()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "CL"):
        if((Student_cl.objects.order_by('-id')).exists()):
            idobj=Student_cl.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        id=""
        id=id+year+branch+"US"+str(lid).zfill(4)
        data = Student_cl()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')
    else:
        return render(request, 'adminloginapp/invalid.html')

#def insertfaculty(request):

    branch = request.POST.get('branch', '')
    date = request.POST.get('bdate', '')
    length = len(date)
    passw = ""
    month = ""
    dat = ""
    year = ""
    for i in range(0, 4):
        year += date[i]
    for i in range(5, 7):
        month += date[i]
    for i in range(8, 10):
        dat += date[i]
    passw = dat+"/"+month+"/"+year
    
    if(branch == "CE"): 
        if((Faculty_ce.objects.order_by('-id')).exists()):
            idobj=Faculty_ce.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4) 
        data = Faculty_ce()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')
    elif(branch == "EC"):
        #idobj = Faculty_ec.objects.order_by('-id')[0]
        if((Faculty_ec.objects.order_by('-id')).exists()):
            idobj=Faculty_ec.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4)
        data = Faculty_ec()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "IT"):
        #idobj = Faculty_it.objects.order_by('-id')[0]
        if((Faculty_it.objects.order_by('-id')).exists()):
            idobj=Faculty_it.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4)
        data = Faculty_it()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "MH"):
        #idobj = Faculty_mh.objects.order_by('-id')[0]
        if((Faculty_mh.objects.order_by('-id')).exists()):
            idobj=Faculty_mh.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4)
        data = Faculty_mh()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "CH"):
        #idobj = Faculty_ch.objects.order_by('-id')[0]
        if((Faculty_ch.objects.order_by('-id')).exists()):
            idobj=Faculty_ch.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4)
        data = Faculty_ch()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "IC"):
        #idobj = Faculty_ic.objects.order_by('-id')[0]
        if((Faculty_ic.objects.order_by('-id')).exists()):
            idobj=Faculty_ic.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        #lid=int(idobj.id)+1
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4)
        data = Faculty_ic()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')

    elif(branch == "CL"):
        if((Faculty_cl.objects.order_by('-id')).exists()):
            idobj=Faculty_cl.objects.order_by('-id')[0]
            lid=int(idobj.id)+1
        else:
            lid=1
        now = datetime.datetime.now()
        year=now.strftime("%Y")[-2:]
        id=""
        id=id+year+branch+"UF"+str(lid).zfill(4)
        data = Faculty_cl()
        data.fname = request.POST.get('fname', '')
        data.lname = request.POST.get('lname', '')
        data.gender = request.POST.get('gender', '')
        data.bdate = request.POST.get('bdate', '')
        data.branch = request.POST.get('branch', '')
        data.mno = request.POST.get('mno', '')
        data.email = request.POST.get('email', '')
        data.password = passw
        data.userid=id
        data.save()
        return render(request, 'adminloginapp/inserted.html')
    else:
        return render(request, 'adminloginapp/invalid.html')

def insert(request):
    c = {}
    c.update(csrf(request))
    if 'user' not in request.session:
        return render(None, 'adminloginapp/login.html',c)
    validate=request.POST.get('validate','')
    branch = request.POST.get('branch', '')
    if(validate=="student"):
        date = request.POST.get('bdate', '')
        length = len(date)
        passw = ""
        month = ""
        dat = ""
        year = ""
        for i in range(0, 4):
            year += date[i]
        for i in range(5, 7):
            month += date[i]
        for i in range(8, 10):
            dat += date[i]
        passw = dat+"/"+month+"/"+year
    
        if(branch == "CE"): 
            if((Student_ce.objects.order_by('-id')).exists()):
                idobj=Student_ce.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.datetime.now()
            year=now.strftime("%Y")[-2:]
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4) 
            data = Student_ce()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})
        elif(branch == "EC"):
            #idobj = Student_ec.objects.order_by('-id')[0]
            if((Student_ec.objects.order_by('-id')).exists()):
                idobj=Student_ec.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4)
            data = Student_ec()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.regtime=datetime.datetime.now()
            data.password = passw
            data.userid=id
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "IT"):
            #idobj = Student_it.objects.order_by('-id')[0]
            if((Student_it.objects.order_by('-id')).exists()):
                idobj=Student_it.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4)
            data = Student_it()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "MH"):
            #idobj = Student_mh.objects.order_by('-id')[0]
            if((Student_mh.objects.order_by('-id')).exists()):
                idobj=Student_mh.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4)
            data = Student_mh()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "CH"):
            #idobj = Student_ch.objects.order_by('-id')[0]
            if((Student_ch.objects.order_by('-id')).exists()):
                idobj=Student_ch.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4)
            data = Student_ch()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "IC"):
            #idobj = Student_ic.objects.order_by('-id')[0]
            if((Student_ic.objects.order_by('-id')).exists()):
                idobj=Student_ic.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4)
            data = Student_ic()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "CL"):
            if((Student_cl.objects.order_by('-id')).exists()):
                idobj=Student_cl.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            id=""
            id=id+year+branch+"US"+str(lid).zfill(4)
            data = Student_cl()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

    else:
        date = request.POST.get('bdate', '')
        length = len(date)
        passw = ""
        month = ""
        dat = ""
        year = ""
        for i in range(0, 4):
            year += date[i]
        for i in range(5, 7):
            month += date[i]
        for i in range(8, 10):
            dat += date[i]
        passw = dat+"/"+month+"/"+year
    
        if(branch == "CE"): 
            if((Faculty_ce.objects.order_by('-id')).exists()):
                idobj=Faculty_ce.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.datetime.now()
            year=now.strftime("%Y")[-2:]
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4) 
            data = Faculty_ce()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})
        elif(branch == "EC"):
            #idobj = Faculty_ec.objects.order_by('-id')[0]
            if((Faculty_ec.objects.order_by('-id')).exists()):
                idobj=Faculty_ec.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4)
            data = Faculty_ec()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "IT"):
            #idobj = Faculty_it.objects.order_by('-id')[0]
            if((Faculty_it.objects.order_by('-id')).exists()):
                idobj=Faculty_it.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4)
            data = Faculty_it()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "MH"):
            #idobj = Faculty_mh.objects.order_by('-id')[0]
            if((Faculty_mh.objects.order_by('-id')).exists()):
                idobj=Faculty_mh.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4)
            data = Faculty_mh()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "CH"):
            #idobj = Faculty_ch.objects.order_by('-id')[0]
            if((Faculty_ch.objects.order_by('-id')).exists()):
                idobj=Faculty_ch.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4)
            data = Faculty_ch()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "IC"):
            #idobj = Faculty_ic.objects.order_by('-id')[0]
            if((Faculty_ic.objects.order_by('-id')).exists()):
                idobj=Faculty_ic.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            #lid=int(idobj.id)+1
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4)
            data = Faculty_ic()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})

        elif(branch == "CL"):
            if((Faculty_cl.objects.order_by('-id')).exists()):
                idobj=Faculty_cl.objects.order_by('-id')[0]
                lid=int(idobj.id)+1
            else:
                lid=1
            now = datetime.now()
            year=now.strftime("%Y")[-2:]
            id=""
            id=id+year+branch+"UF"+str(lid).zfill(4)
            data = Faculty_cl()
            data.fname = request.POST.get('fname', '')
            data.mname=request.POST.get('mname','')
            data.lname = request.POST.get('lname', '')
            data.gender = request.POST.get('gender', '')
            data.bdate = request.POST.get('bdate', '')
            #data.branch = request.POST.get('branch', '')
            data.mno = request.POST.get('mno', '')
            data.email = request.POST.get('email', '')
            data.password = passw
            data.userid=id
            data.regtime=datetime.datetime.now()
            data.save()
            return render(request, 'adminloginapp/inserted.html',{'userid':id,'password':passw})


def logout(request):
    c = {}
    c.update(csrf(request))
    if 'user' not in request.session:
        return render(None, 'adminloginapp/login.html',c)
    del request.session['user']
    return render(None, 'adminloginapp/login.html',c)