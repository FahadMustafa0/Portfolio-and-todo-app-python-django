from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.webpage, name='web'),
    path('home/',views.webpage,name ='home'),
    path('contact/', views.kontact, name='kontact'),
    path('services/', views.services, name='services'),
    path('about/', views.abot, name='about'),
    path('index/', views.index, name='index'),
    path('login/', views.loginUser, name='login'),
    path('logoutuser/', views.logoutUser, name='logout'),
    path('admin/', admin.site.urls),
    path('todoapp/', views.todoapp,name='todoapp'),
    path('delete_todo/<int:todo_id>/', views.todelete,name='delete_todo'),

    ]
