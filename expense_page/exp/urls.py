from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginPage,name= 'login'),
     path('logout/',views.loginPage,name= 'logout'),
    


    path('',views.home,name='home'),
    
    path('expense/',views.expense,name='expense'),

    path('create_expense/', views.createExpense, name='create_expense'),
    path('update_expense/<str:pk>/', views.updateExpense, name='update_expense'),
    path('delete_expense/<str:pk>/', views.deleteExpense, name='delete_expense'),

]
