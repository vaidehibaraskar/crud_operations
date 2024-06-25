from django.shortcuts import render, HttpResponse, redirect
from .models import Person
from .forms import PersonForm

# Create your views here.
def homeview(request):
    return render(request,"app1/home.html",{})


def addview(request):
    form = PersonForm()
    if request.method=="POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"app1/add.html",{"form":form})

def showview(request):
    per = Person.objects.all()
    return render(request,"app1/show.html",{"obj":per})

def updateview(request,pk):
    obj = Person.objects.get(pid = pk)
    form = PersonForm(instance=obj)
    if request.method=="POST":
        form = PersonForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"app1/add.html",{"form":form})


def deleteview(request,x):
    obj = Person.objects.get(pid = x)
    if request.method=="POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"app1/success.html",{"obj":obj})