from django.db import models
from django.urls import reverse

INCOMETYPES = (
  ('Earned', 'Earned'),
  ('Passive', 'Passive'),
  ('Portfolio', 'Porfolio'),
)

# Create your models here.
class Income(models.Model):
   name = models.CharField(max_length=100)
   category = models.CharField(
    max_length=10,
    choices=INCOMETYPES,
    default=INCOMETYPES[0][0]
  )
   amount = models.IntegerField()
   
   def __str__(self):
     return self.name
   
   def get_absolute_url(self):
        return reverse('incomes_detail', kwargs={'income_id': self.id})

class Expense(models.Model):
   name = models.CharField(max_length=100)
   category = models.CharField(max_length=100)
   amount = models.IntegerField()
   
   def __str__(self):
     return self.name
   
   def get_absolute_url(self):
        return reverse('expenses_detail', kwargs={'expense_id': self.id})

class Bill(models.Model):
   name = models.CharField(max_length=100)
   category = models.CharField(max_length=100)
   amount = models.IntegerField()
   
   def __str__(self):
     return self.name
   
   def get_absolute_url(self):
        return reverse('bills_detail', kwargs={'bill_id': self.id})