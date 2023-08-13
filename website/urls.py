from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login_user,name='login'),
   path('logout/',views.logout_user,name='logout'),
   path('register/',views.register_user,name='register'),
   path('records/',views.records,name='records'),
   path('record/<int:pk>', views.customer_records, name='record'),
]
