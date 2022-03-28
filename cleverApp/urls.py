from django.urls import path, include
from django.conf import urls
from . import views
from cleverApp.views import common, members,super_user
from django.contrib.auth import views as auth_views

urlpatterns = [

   
    path('About', common.About.as_view(), name="About"),
    path('Services', common.Services.as_view(), name="Services"),
    # path('properties', common.Properties.as_view(), name="properties"),
    path('Contact', common.contact, name='Contact'),
    path('signup', common.MemberSignupView.as_view(), name="signup"),
    path('login/',common.login_request,name='login'),
    path('logout/',common.logout_view, name='logout'),

    # user urls
    path('UpdateProfile/<int:pk>',members.get_profile,name='UpdateProfile'),
    path('MemberProfile/<int:pk>',members.MemberProfileDetailView.as_view(),name='MemberProfile'),
    
    

    #  Admin Urls
    path('users', super_user.users_list, name= 'users'),
    path('activate/<int:pk>', super_user.activate_user, name = 'activate_data'),
    path('deactivate/<int:pk>',super_user.deactivate_user, name = 'deactivate_data'),

    path('Post_form',members.PostCreateView.as_view(),name='Post_form'),
    path('Edit_Post/<int:pk>',members. UpdateRecs.as_view(),name='Edit_Post'),
    path('properties',members.PostListView.as_view(),name='properties'),
    path('property_detail/<int:pk>',members.PostDetailView.as_view(),name='property_detail'),
    path('update/<int:pk>',members.UpdateRecs.as_view(),name='update'),
    path('delete/<int:pk>',members.DeletePost.as_view(),name='delete'),
    path ('add_category', members.AddCategory.as_view(), name = 'add_category'),
    path('drafted_properties',members.DraftListView.as_view(),name='drafted_properties'),
    path("publish/<int:pk>",members.publish_drafts_post,name="publish"), 
    path('category/<str:cats>/', members.CategoryView, name='category'),
    path('staffs',members.MemberList.as_view(), name='staffs'),

]