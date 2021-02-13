from django.shortcuts import render,HttpResponseRedirect
from .forms import Createuser
from django.contrib.auth import authenticate,login
from django.urls import reverse,reverse_lazy
# Create your views here.

def signup(request):
    form=Createuser()
    register=False
    if request.method =='Post':
        form=Createuser(data=request.Post)
        if form.is_valid():
         user=form.save()
         register=True
         pass
    dictt={'form':form}
    return render(request, 'App_Login/signup.html', context={'title': 'Sign up . Social', 'form': form})



