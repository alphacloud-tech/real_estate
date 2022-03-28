from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  User,Member, Contact



admin.site.register(User)
admin.site.register(Member)
admin.site.register(Contact)