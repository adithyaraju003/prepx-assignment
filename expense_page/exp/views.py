from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import ExpenseForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate,login, logout

# Create your views here.

def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password does not exist')


    context= {}
    return render(request,'exp/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    expenses = Expense.objects.all()
   
    return render(request,'exp/dashboard.html',{'expenses':expenses})



def expense(request):
   
    return render(request,'exp/expense.html',)

def createExpense(request):
    
    form = ExpenseForm()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form' :form}
    return render(request, 'exp/expense_form.html',context)

def updateExpense(request, pk):
    expense = Expense.objects.get(id = pk)
    form = ExpenseForm( instance= expense)

    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance= expense)
        if form.is_valid():
            form.save()
            return redirect('/')

    context ={'form':form}
    
    return render(request, 'exp/expense_form.html',context)

def deleteExpense(request , pk):
     expense = Expense.objects.get(id = pk)
     if request.method == "POST":
        expense.delete()
        return redirect('/')
         
     context = {'item':expense}
     return render(request, 'exp/delete.html',context)


