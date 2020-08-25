from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authapp.forms import signupform
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'testapp/home.html')

@login_required
def java(request):
    return render(request,'testapp/java.html')

@login_required
def python(request):
    return render(request,'testapp/python.html')

@login_required
def aptitude(request):
    return render(request,'testapp/aptitude.html')

def logout(request):
    return render(request,'testapp/logout.html')

def signup(request):
    form=signupform()
    if request.method=='POST':
        form=signupform(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
