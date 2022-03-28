from django import forms
from .models import (User, Member, Post, Category, Contact)
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.core.exceptions import ValidationError
from ckeditor.widgets import CKEditorWidget


class MemberRegistrationForm(UserCreationForm):
    first_name      = forms.CharField(required=False)
    last_name       = forms.CharField(required=False)
    email           = forms.EmailField(required=True)
    phone_no        = forms.CharField(required=True)
    address         = forms.CharField(required=True)
    password1 = forms.PasswordInput()
    password2= forms.PasswordInput()
    
    class Meta(UserCreationForm.Meta):
        model = User
    
        fields = ['username','first_name','last_name','email','phone_no','address', 'password1', 'password2']
        

        
        widgets = {
                'first_name':forms.TextInput(attrs={'class':'form-control','type':'hidden'}),
                'last_name':forms.TextInput(attrs={'class':'form-control','type':'hidden'}),
                'phone_no':forms.TextInput(attrs={'class':'form-control','type':'hidden'}),
                'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
                'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Address'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = ''
        self.fields['username'].widget.attrs['class'] = 'form-control  border border-info' 

        self.fields['first_name'].widget.attrs['placeholder'] = ''
        self.fields['first_name'].widget.attrs['class'] = 'form-control border border-info' 
        
        self.fields['last_name'].widget.attrs['placeholder'] = ''
        self.fields['last_name'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['phone_no'].widget.attrs['placeholder'] = ''
        self.fields['phone_no'].widget.attrs['class'] = 'form-control border border-info'  


        self.fields['address'].widget.attrs['placeholder'] = ''
        self.fields['address'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['password1'].widget.attrs['placeholder'] = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['password2'].widget.attrs['placeholder'] = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control border border-info'
       
    @transaction.atomic
    def save(self, commit=False):
        user= super().save(commit=commit)
        user.is_member = True
        user.email  = self.cleaned_data.get("email")
        user.save()
        member = Member.objects.create(user=user)
        member.phone_no       = self.cleaned_data.get('phone_no')
        member.address        = self.cleaned_data.get('address')
        member.save()
        return user


        # Member update Profile Registration form
class UpdateForm(UserChangeForm):
    class Meta:
        model = Member
        fields = [ 'phone_no', 'address',  'photograph']
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
        self.fields['address'].widget.attrs['placeholder'] = 'address'
        self.fields['address'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['photograph'].widget.attrs['placeholder'] = 'photograph'
        self.fields['photograph'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['phone_no'].widget.attrs['placeholder'] = 'phone_no'
        self.fields['phone_no'].widget.attrs['class'] = 'form-control border border-info' 




choices = Category.objects.all().values_list('category_name', 'category_name') #in ur widgets u cn use choices = choices but adversable loop through it for it to be logical like this
choice_list = []
for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['Poster_Name', 'property_title', 'property_status','property_address', 'Main_building', 'sub_building1','sub_building2','sub_building3','sub_building4', 'property_category' , 'property_discription']


        widgets = {
           
            
            'property_status': forms.Select(choices=choices, attrs={'class':'form-control'}), #first way
            'property_category': forms.Select(choices=choice_list, attrs={'class':'form-control'}), #second wa
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Poster_Name'].widget.attrs['placeholder'] = 'Poster_Name'
        self.fields['Poster_Name'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['property_title'].widget.attrs['placeholder'] = 'property_title'
        self.fields['property_title'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['property_status'].widget.attrs['placeholder'] = 'property_status'
        self.fields['property_status'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['Main_building'].widget.attrs['placeholder'] = 'Main_building'
        self.fields['Main_building'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['sub_building1'].widget.attrs['placeholder'] = 'sub_building1'
        self.fields['sub_building1'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['sub_building2'].widget.attrs['placeholder'] = 'sub_building2'
        self.fields['sub_building2'].widget.attrs['class'] = 'form-control border border-info' 
        
        self.fields['sub_building3'].widget.attrs['placeholder'] = 'sub_building3'
        self.fields['sub_building3'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['sub_building4'].widget.attrs['placeholder'] = 'sub_building34'
        self.fields['sub_building4'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['property_category'].widget.attrs['placeholder'] = 'property_category'
        self.fields['property_category'].widget.attrs['class'] = 'form-control border border-info'

        # self.fields['property_discription'].widget.attrs['placeholder'] = ''
        # self.fields['property_discription'].widget.attrs['class'] = 'form-control border border-info col-lg-8 col-md-8 col-sm-12' 

        self.fields['property_address'].widget.attrs['placeholder'] = ''
        self.fields['property_address'].widget.attrs['class'] = 'form-control border border-info' 


class EditPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = [ 'property_title', 'property_status', 'property_address',  'Main_building', 'sub_building1','sub_building2','sub_building3','sub_building4', 'property_category', 'property_discription']


        widgets = {
           
            
            'property_status': forms.Select(choices=choices, attrs={'class':'form-control'}), #first way
            'property_category': forms.Select(choices=choice_list, attrs={'class':'form-control'}), #second wa
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        self.fields['property_title'].widget.attrs['placeholder'] = 'property_title'
        self.fields['property_title'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['property_status'].widget.attrs['placeholder'] = 'property_status'
        self.fields['property_status'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['Main_building'].widget.attrs['placeholder'] = 'Main_building'
        self.fields['Main_building'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['sub_building1'].widget.attrs['placeholder'] = 'sub_building1'
        self.fields['sub_building1'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['sub_building2'].widget.attrs['placeholder'] = 'sub_building2'
        self.fields['sub_building2'].widget.attrs['class'] = 'form-control border border-info' 
        
        self.fields['sub_building3'].widget.attrs['placeholder'] = 'sub_building3'
        self.fields['sub_building3'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['sub_building4'].widget.attrs['placeholder'] = 'sub_building34'
        self.fields['sub_building4'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['property_category'].widget.attrs['placeholder'] = 'property_category'
        self.fields['property_category'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['property_discription'].widget.attrs['placeholder'] = ''
        self.fields['property_discription'].widget.attrs['class'] = 'form-control border border-info' 

        self.fields['property_address'].widget.attrs['placeholder'] = ''
        self.fields['property_address'].widget.attrs['class'] = 'form-control border border-info' 



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['category_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs['placeholder'] = 'category_name'
        self.fields['category_name'].widget.attrs['class'] = 'form-control border border-info' 

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')

        if not category_name:
            raise forms.ValidationError('This field is requied!')

        for instance in Category.objects.all():
            if instance.category_name == category_name:
                raise forms.ValidationError(str(category_name) + ' is already created')
        return category_name




class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number',  'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = ''
        self.fields['name'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['email'].widget.attrs['placeholder'] = ''
        self.fields['email'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['phone_number'].widget.attrs['placeholder'] = ''
        self.fields['phone_number'].widget.attrs['class'] = 'form-control border border-info'

        self.fields['message'].widget.attrs['placeholder'] = ''
        self.fields['message'].widget.attrs['class'] = 'form-control border border-info'

       