from django.shortcuts import render,HttpResponseRedirect
from .forms import *

# Create your views here.

# This function will add student and show the student 
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    Stud = User.objects.all()
    return render(request,"enroll/addandshow.html",{"form":fm,"stu":Stud})

# This function is responsible for updating data
def update_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request,"enroll/updatestudent.html",{"form":fm})
# For deleting student 
def delete_data(request,id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')