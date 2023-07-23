from django.urls import path
from . import views

urlpatterns = [
    #All posts on one page
    path('', views.post_list, name='post_list'),
    #Individual posts displayed on their own page
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]