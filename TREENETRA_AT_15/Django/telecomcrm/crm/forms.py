from django import forms
from django.contrib.auth.models import User
from .models import Plan


# Sign-up form including additional phone number field
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # Create the related UserProfile record
            from .models import UserProfile
            UserProfile.objects.create(user=user, phone_number=self.cleaned_data['phone_number'])
        return user


# Simple login form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


# Form for plan selection
class PlanSelectionForm(forms.Form):
    plan_type = forms.ChoiceField(choices=(
        ('Prepaid', 'Prepaid'),
        ('Postpaid', 'Postpaid'),
        ('Broadband', 'Broadband'),
    ))
    # Only required if Prepaid is selected
    prepaid_plan = forms.ChoiceField(choices=(
        ('call', 'Call'),
        ('sms', 'SMS'),
        ('datapack', 'Data Pack'),
    ), required=False)
    billing_cycle = forms.ChoiceField(choices=(
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
    ), required=False)


# Payment form for billing/invoice page
class PaymentForm(forms.Form):
    order_id = forms.IntegerField(widget=forms.HiddenInput)
    payment_type = forms.ChoiceField(choices=(
        ('credit', 'Credit Card'),
        ('debit', 'Debit Card'),
    ))
