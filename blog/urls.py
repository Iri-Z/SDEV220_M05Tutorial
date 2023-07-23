from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as v2
from . import views

urlpatterns = [
    #All posts on one page
    path('', views.post_list, name='post_list'),
    #Individual posts displayed on their own page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #Request for creating new posts
    path('post/new/', views.post_new, name='post_new'),
    #Request for edit page
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    #Login page
    path('accounts/login/', v2.LoginView.as_view(), name='login'),
    #Drafts page
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    #Send draft to be published
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    #Delete a post
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    #Create comment request
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    #Comment moderation
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]