from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView,ListView,CreateView,DetailView,UpdateView,DeleteView
from cleverApp.models import (User, Member, Post, Contact)
from django.contrib import messages #import messages
from django.http import HttpResponse
from cleverApp.forms import (MemberRegistrationForm, Member, ContactForm)
from django.utils import timezone


class Home(ListView):
    template_name = 'webApp/index-3.html'
    model = Post
    context_object_name ="post_list"
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
        recent_properties                         = Post.objects.all()[0:4]
        post_count                                = Post.objects.count()
        context                                   = super(ListView, self).get_context_data(*args,**kwargs)
        context['recent_properties']              =  recent_properties 
        context['post_count']       = post_count
        return context
    
class About(TemplateView):
    template_name = "webApp/about.html"

    def get_context_data(self, *args, **kwargs):
        post_count                  = Post.objects.count()
        context = super(TemplateView, self).get_context_data(*args,**kwargs)
        context['post_count']       = post_count
        return context


class Services(TemplateView):
    template_name = "webApp/services-1.html"

    def get_context_data(self, *args, **kwargs):
        post_count                  = Post.objects.count()
        context = super(TemplateView, self).get_context_data(*args,**kwargs)
        context['post_count']       = post_count
        return context


# class Contact(TemplateView):
#     template_name = "webApp/contact.html"



def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :

                if user.is_member:
                    login(request,user)
                    return redirect('properties')

               
                if user.is_superuser:
                    login(request,user)
                    return redirect('properties')
                
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, 'webApp/login.html',context={'form':AuthenticationForm()})

def logout_view(request):
    logout(request)
    return redirect('/')


class MemberSignupView(CreateView):
    model           = Member
    form_class      = MemberRegistrationForm
    template_name   = 'webApp/signup.html'


    def form_valid(self, form):
            user = form.save()
            login(self.request, user)
            return redirect('properties')



def contact(request):

        saveFlag = False
        newform = ContactForm()
        if request.method == "POST":

            newform = ContactForm(request.POST)
            names = mail = mess = phone = ""

            if newform.is_valid():        
                names      = request.POST['name']
                mail      = request.POST.get("email")
                mess      = request.POST['message']
                phone = request.POST['phone_number']

                newform  = Contact(name = names, email=mail,  message = mess, phone_number = phone,)
                saveFlag  = newform.save()
                saveFlag = True
                
            if saveFlag:
                message = {
                            "response":"Thank you for contacting us, We will revert back shortly",
                            "name": names
                        }
            else:
                message = {
                            "form":newform
                        }
        else:
            message = { "form":newform}

        return render(request,'webApp/contact.html', context = message)