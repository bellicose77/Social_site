from django.shortcuts import render,HttpResponseRedirect
from .forms import CreateNewUser
from django.contrib.auth import authenticate,login
from django.urls import reverse,reverse_lazy
# Create your views here.

def signup(request):
    form=CreateNewUser()
    register=False
    if request.method =='Post':
        form= CreateNewUser(data=request.Post)
        if form.is_valid():
         user= form.save()
         register=True
         pass
    context={'form':form}

    return render(request, 'App_loging/signup.html', context)



