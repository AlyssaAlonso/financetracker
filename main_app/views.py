from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Income, Bill, Expense

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finances(request):
  return render(request, 'finances.html')

def incomes_index(request):
  incomes = Income.objects.all()
  return render(request, 'incomes/index.html', {
    'incomes': incomes
  })

def incomes_detail(request, income_id):
  income = Income.objects.get(id=income_id)
  return render(request, 'incomes/detail.html', {
    'income': income,
  })

class IncomeCreate(CreateView):
  model = Income
  fields = '__all__'

class IncomeUpdate(UpdateView):
  model = Income
  fields = '__all__'

class IncomeDelete(DeleteView):
  model = Income
  success_url = '/incomes'

def bills_index(request):
  bills = Bill.objects.all()
  return render(request, 'bills/index.html', {
    'bills': bills
  })

def bills_detail(request, bill_id):
  bill = Bill.objects.get(id=bill_id)
  return render(request, 'bills/detail.html', {
    'bill': bill,
  })

class BillCreate(CreateView):
  model = Bill
  fields = '__all__'

class BillUpdate(UpdateView):
  model = Bill
  fields = '__all__'

class BillDelete(DeleteView):
  model = Bill
  success_url = '/bills'

def expenses_index(request):
  expenses = Expense.objects.all()
  return render(request, 'expenses/index.html', {
    'expenses': expenses
  })

def expenses_detail(request, expense_id):
  expense = Expense.objects.get(id=expense_id)
  return render(request, 'expenses/detail.html', {
    'expense': expense,
  })

class ExpenseCreate(CreateView):
  model = Expense
  fields = '__all__'

class ExpenseUpdate(UpdateView):
  model = Expense
  fields = '__all__'

class ExpenseDelete(DeleteView):
  model = Expense
  success_url = '/expenses'