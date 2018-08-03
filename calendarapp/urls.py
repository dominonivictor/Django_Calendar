#Here are the url that "control" pages, directing requests to each path
#He goes into myapp/views.py to render the page (if needed)
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calendar', views.calendar, name='calendar'), #Main Calandar Page
    path('', views.index, name='index'), #Start Page
    path('entry/<int:pk>', views.details, name='details'),#Informs a specific event details
    path('entry/add', views.add, name='add'),#Adds a new event/date
    path('entry/delete/<int:pk>', views.delete, name='delete'), #Deletes an entry, without changing pages
    path('login', auth_views.login, name='login'), #Login Page
    path('logout', auth_views.logout, {'next_page': '/'}, name='logout'),#Logs out current user
    path('signup', views.signup, name='signup'),#Signs up a new user
]
