from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
from cleverApp.models import (User, Member)


def users_list(request):
    model = User
    results = User.objects.all()
    return render(request,'webApp/users_list.html', {'results':results})

def activate_user(request, pk):
    staff =get_object_or_404(User, pk=pk)
    staff.is_staff = True
    staff.save()
    model = User
    results = User.objects.all()
    return render(request,'webApp/users_list.html', {'results':results})


def deactivate_user(request,pk):
    user = get_object_or_404(User, pk=pk)
    user.is_staff = False
    user.save()
    model = User
    results = User.objects.all()
    return render(request,'webApp/users_list.html', {'results':results})