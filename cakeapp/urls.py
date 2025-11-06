from django.contrib import admin
from django.urls import path
from cakeapp import views

urlpatterns = [
    path('',views.index),
    path('adminlogin',views.adminlogin),
    path('adminhome',views.adminhome),
    path('dashboard',views.dashboard),
    path('checklogin',views.checklogin),
    path('addcakes',views.addcakes),
    path('addproducts',views.addproducts),
    path('viewall',views.viewall),
    path('selectcake/<int:id>',views.selectcake),
    path('deletecake/<int:id>',views.deletecake),
    path('modifycake/<int:id>',views.modifycake),
    path('updatecakes/<int:id>',views.updatecakes),
    path('cakebehome',views.cakebehome),
]