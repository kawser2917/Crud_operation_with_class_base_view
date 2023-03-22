from django.shortcuts import render,HttpResponseRedirect
from .forms import *
from django.views.generic.base import TemplateView, RedirectView

# Create your views here.

# This function will add student and show the student
class AddShow(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self,*args,**kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        stud = User.objects.all()
        context = {"form":fm,"stu":stud}
        return context
    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
            return HttpResponseRedirect('/')



# def add_show(request):
#     if request.method == "POST":
#         fm = StudentRegistration(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = StudentRegistration()
#     else:
#         fm = StudentRegistration()
#     Stud = User.objects.all()
#     return render(request,"enroll/addandshow.html",{"form":fm,"stu":Stud})

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
class DeleteData(RedirectView):
    url = '/'
    def get_redirect_url(self,*args,**kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args,**kwargs)


# def delete_data(request,id):
#     if request.method == "POST":
#         pi = User.objects.get(pk=id)
#         pi.delete()
#         return HttpResponseRedirect('/')