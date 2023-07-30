from django.db import models

# Create your models here.
# expense_app/models.py

class Customer(models.Model):
    name = models.CharField(max_length= 200, null=True)
    phone = models.CharField(max_length=200, null =True)
    email = models.CharField(max_length=200, null = True)
    date_created = models.DateTimeField(auto_now_add= True, null =True)

    def __str__(self):
        return self.name

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Health', 'Health'),
        ('Electronics', 'Electronics'),
        ('Travel', 'Travel'),
        ('Education', 'Education'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]

    name = models.CharField(max_length=140)
    date = models.DateField(auto_now_add= True, null =True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    amount = models.PositiveIntegerField()
    created_by = models.CharField(max_length=200)  # Assuming you store member ID as a string
    created_at = models.DateTimeField(auto_now_add=True,null =True)
    updated_at = models.DateTimeField(auto_now=True,null =True)

    def __str__(self):
        return self.name
