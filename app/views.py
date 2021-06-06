
from datetime import datetime
from django.utils import timezone
from django.shortcuts import render,HttpResponse ,redirect
from django.http import HttpRequest
from app.models import Contact,todo
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
g=""

def webpage(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'webpage.html')

def newlayout(request):
    return render(request,'newwebpage.html')
    

def kontact(request):
# this the handelling of posted form and saving its data to db
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
    'variable' : "test"}   
     return render(request,'abot.html',context)

def index(request):
    return render(request,'index.html')
# authentication system
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
# Create Operation
    if request.method=="POST":
        item=request.POST.get('item')
        dato=timezone.now()
        todoobj=todo(date=dato,text=item)
        todoobj.save()
    # f=todo.objects.all().create(date=dato,text=item)
    # somwthing=Contact.objects.all()

# Read Operation
    todo_items=todo.objects.all().order_by("date")     
    return render(request, "todoapp.html",{ "todo_items" : todo_items})

def toedit(request,todo_id):
    ins=todo.objects.get(id=todo_id)
    global g 
    g= ins
    return render(request, "edit.html")

# Update operation
def to(request):
    if request.method=="POST":
        it=request.POST.get('textfield')
        g.text=it
        g.save()
        return redirect("/todoapp")

# Delete operation   
def todelete(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return redirect("/todoapp")

