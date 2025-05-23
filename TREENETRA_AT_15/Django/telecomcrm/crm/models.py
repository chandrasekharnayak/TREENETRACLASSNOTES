from django.db import models
from django.contrib.auth.models import User

# Choices for various fields
PLAN_CHOICES = (
    ('Prepaid', 'Prepaid'),
    ('Postpaid', 'Postpaid'),
    ('Broadband', 'Broadband'),
)

PREPAID_PLAN_CHOICES = (
    ('call', 'Call'),
    ('sms', 'SMS'),
    ('datapack', 'Data Pack'),
)

BILLING_CYCLE_CHOICES = (
    ('monthly', 'Monthly'),
    ('quarterly', 'Quarterly'),
)

ORDER_STATUS_CHOICES = (
    ('pending', 'Pending'),
    ('activated', 'Activated'),
    ('completed', 'Completed'),
)

PAYMENT_TYPE_CHOICES = (
    ('credit', 'Credit Card'),
    ('debit', 'Debit Card'),
)

# Extend the built-in User model with a profile (phone number)
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username

# Model to store plan details
class Plan(models.Model):
    plan_type = models.CharField(max_length=20, choices=PLAN_CHOICES)
    # Only applicable for prepaid plans
    prepaid_plan = models.CharField(max_length=20, choices=PREPAID_PLAN_CHOICES, blank=True, null=True)
    billing_cycle = models.CharField(max_length=20, choices=BILLING_CYCLE_CHOICES, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        detail = f" - {self.prepaid_plan}" if self.prepaid_plan else ""
        return f"{self.plan_type}{detail}"

# Model to track orders
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"

# Model to track billing and payment information
class Billing(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_TYPE_CHOICES)
    payment_status = models.BooleanField(default=False)
    billing_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Billing for Order #{self.order.id}"
