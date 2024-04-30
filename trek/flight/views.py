from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def homepage(request):
    return render(request,'home.html')

def ulogin(request):
    a={}
    if request.method == 'GET':
        return render(request,'login.html')
    
    else:
        uname=request.POST['uname']
        upa=request.POST['upass']
        print("email:",uname, upa)
        if uname == '' or upa == '':
            a['error']="please fill the fields below"
            return render(request, 'login.html',a)
        else:
            b=authenticate(username=uname, password=upa)
            print("creditianal :",b)
            if b is not None :
                login(request,b)
                return redirect('/')
            else:
                a['error']='invalid E-mail and Password'
                return render(request,'login.html',a)
        




def register(request):
    a={}
    b={}
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        uname=request.POST['username']
        e=request.POST['email']
        ph=request.POST['ph']
        pa=request.POST['pass']
        cp=request.POST['cpass']
        if uname == '' or e == '' or ph == '' or cp == '':
            b['error']="fields are empty "
            return render(request,'register.html',b)
        elif pa!=cp:
            b['ps']="password didn't match"
            return render(request,'register.html',b)
        else:
            a=User.objects.create(username=uname, email=e, password=pa)
            # a.set_password(pa)
            a.save()
            b['success']="user registered successfully"
            return render(request,'register.html',b)

def booking(request):
    return render(request,'booking.html')

def booking1(request):
    return render(request,'booking1.html')

def booking2(request):
    return render(request,'booking2.html')

def booktickets(request):
    return render(request,'booktickets.html')
# Create your views here.
