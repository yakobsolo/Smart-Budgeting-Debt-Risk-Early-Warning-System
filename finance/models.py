from django.db import models
from django.conf import settings

class Income(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    source = models.CharField(max_length=255)
    date = models.DateField()
    recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.amount}"

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('rent', 'Rent'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField()
    date = models.DateField()
    recurring = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.amount}"

class Debt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.FloatField()
    minimum_payment = models.DecimalField(max_digits=12, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.total_amount}"
