from datetime import datetime
from django.utils import timezone
from django.shortcuts import render,HttpResponse ,redirect
from django.http import HttpRequest
from app.models import Contact,todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login


def webpage(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'webpage.html')
def kontact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        msg=request.POST.get('msg')
        contact= Contact(name=name,email=email,msg=msg)   
        contact.save()
        messages.success(request,'Message sent successfully!')
    return render(request,'kontact.html')
def services(request):
    return render(request,'services.html')
def abot(request):
     context={
    'variable' : "fahad"}   
     return render(request,'abot.html',context)
def index(request):
    return render(request,'index.html')
def loginUser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.success(request,'User Not found')
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def todoapp(request):
    if request.method=="POST":
        item=request.POST.get('item')
        dato=timezone.now()
        print(dato)
        todoobj=todo(date=dato,text=item)
        todoobj.save()
        print("fhaad")
    # f=todo.objects.all().create(date=dato,text=item)
    somwthing=Contact.objects.all()
    todo_items= todo.objects.all().order_by("date")     
    return render(request, "todoapp.html",{ "todo_items" : todo_items})

def todelete(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return redirect("/todoapp")

