from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finances/', views.finances, name='finances'),

  path('incomes/', views.incomes_index, name='incomes_index'),
  path('incomes/<int:income_id>/', views.incomes_detail, name='incomes_detail'),
  path('incomes/create/', views.IncomeCreate.as_view(), name='incomes_create'),
  path('incomes/<int:pk>/update/', views.IncomeUpdate.as_view(), name='incomes_update'),
  path('incomes/<int:pk>/delete/', views.IncomeDelete.as_view(), name='incomes_delete'),

  path('bills/', views.bills_index, name='bills_index'),
  path('bills/<int:bill_id>/', views.bills_detail, name='bills_detail'),
  path('bills/create/', views.BillCreate.as_view(), name='bills_create'),
  path('bills/<int:pk>/update/', views.BillUpdate.as_view(), name='bills_update'),
  path('bills/<int:pk>/delete/', views.BillDelete.as_view(), name='bills_delete'),

  path('expenses/', views.expenses_index, name='expenses_index'),
  path('expenses/<int:expense_id>/', views.expenses_detail, name='expenses_detail'),
  path('expenses/create/', views.ExpenseCreate.as_view(), name='expenses_create'),
  path('expenses/<int:pk>/update/', views.ExpenseUpdate.as_view(), name='expenses_update'),
  path('expenses/<int:pk>/delete/', views.ExpenseDelete.as_view(), name='expenses_delete'),
]