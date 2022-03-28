from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils import timezone
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField


class User(AbstractUser):
    first_name              = models.CharField(max_length=100)
    last_name               = models.CharField(max_length=100)
    is_member               = models.BooleanField(default=False)
    # username                = models.CharField(max_length=10) 
    def __str__(self):
        return self.username



class Member(models.Model):
    user            = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no        = models.CharField(max_length=100)
    address         = models.CharField(max_length=100)
    photograph      = models.ImageField(upload_to='featured_image',blank=True)
    
    def __str__(self):
        return self.user

    def get_absolute_url(self):
        return reverse("user_detail", kwargs={"pk": self.pk})


class Post(models.Model):
    property_status_CHOICES = (
        ('for sale', 'FOR SALE'),
        ('for rent', 'FOR RENT'),
        ('other', 'OTHER'),
    )

    Poster_Name             = models.ForeignKey(User,on_delete=models.CASCADE)
    property_title          = models.CharField(max_length=200)
    property_status         = models.CharField(max_length=100,choices=property_status_CHOICES)
    # property_discription    = models.TextField()
    property_discription    = RichTextField(blank=True,null=True)
    
    Main_building           = models.ImageField(upload_to='featured_images',blank=True)
    sub_building1           = models.ImageField(upload_to='featured_images',blank=True)
    sub_building2           = models.ImageField(upload_to='featured_images',blank=True)
    sub_building3           = models.ImageField(upload_to='featured_images',blank=True)
    sub_building4           = models.ImageField(upload_to='featured_images',blank=True)
    created_date            = models.DateTimeField(default=timezone.now())
    published_date          = models.DateTimeField(blank=True,null=True)
    property_category       = models.CharField(max_length=200, default='uncategorised')
    property_address        = models.CharField(max_length=200, default="")
    

    def __str__(self):
        return self.property_title 

    def get_absolute_url(self):
        return reverse('property_detail', kwargs={'pk':self.pk})
    
    def published_post(self):
        self.published_date = timezone.now()
        self.save()


  #    Added Category model
class Category(models.Model): #create new class inorder to be able to delete n change d categories in future
    category_name                = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

    def get_absolute_url(self):
        return reverse ("properties")


class Contact(models.Model):
    name                    = models.CharField(max_length = 128)
    email                   = models.CharField(max_length = 264, unique = True)
    phone_number            = models.CharField(max_length = 128)
    message                 = models.TextField()


    def __str__(self):

        return self.name 

    def get_absolute_url(self):

        return reverse('Contact',)