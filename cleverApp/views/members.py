
from django.http.response import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import TemplateView,ListView, CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from cleverApp.models import (User, Member, Post, Category)
from cleverApp.forms import (UpdateForm, MemberRegistrationForm, PostForm, EditPost,CategoryForm)  
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils import timezone
# from django.db.models import Sum, Count


# updating user profile
def get_profile(request,pk):
    if request.method == 'POST':
        u_form = UpdateForm(request.POST,request.FILES,instance=request.user.member)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('MemberProfile',pk=pk)
        else:
            u_form =  UpdateForm()
    else:
        u_form = UpdateForm(instance=request.user.member)
       
    context = {'u_form':u_form}
    return render(request,"webApp/updateProfile.html",context)


class MemberProfileDetailView(DetailView):
    model = User
    context_object_name = 'user_detail'
    template_name = "webApp/user-profile.html"



class PostCreateView(CreateView):
    form_class = PostForm
    template_name = "webApp/post_form.html"
    model = Post
 
class PostListView(ListView):
    template_name = "webApp/properties-grid-rightside.html"
    model = Post
    context_object_name ="post_list"
    paginate_by = 4
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
        recent_properties                         = Post.objects.all()[0:3]
        cat_menu                                  = Category.objects.all()
        context                                   = super(PostListView, self).get_context_data(*args,**kwargs)
        context['recent_properties']              =  recent_properties 
        context['cat_menu']                       = cat_menu
        return context
    
class PostDetailView(DetailView):
    template_name = "webApp/properties_details.html"
    context_object_name ="post_detail"
    model = Post


class UpdateRecs(UpdateView):
    template_name = "webApp/update_post.html"
    form_class = EditPost
    model = Post


class DeletePost(DeleteView):
    template_name = "webApp/Delete_post.html"
    model = Post
    success_url = reverse_lazy('properties')


class DraftListView(ListView):
    context_object_name = 'drafts'
    model = Post
    template_name = "webApp/drafted_properties.html"
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')


def publish_drafts_post(request,pk):
    post =  get_object_or_404(Post,pk=pk)
    post.published_post()
    return redirect("property_detail", pk=post.pk)


# Category View

class AddCategory(CreateView):
    model = Category
    template_name = 'webApp/add_category.html'
    success_url = reverse_lazy('properties')
    # fields = '__all__'
    form_class = CategoryForm

def CategoryView(request,cats):
    category_post = Post.objects.filter(property_category=cats)#the category is from our model.py by calling category dat equal to cats
    return render(request, 'webApp/categories.html', {'cats': cats, 'category_post':category_post})



class MemberList(ListView):
    model = User
    context_object_name = 'members'
    template_name = "webApp/staffList.html"