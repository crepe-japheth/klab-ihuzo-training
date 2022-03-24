from django import forms

class PaymentForm(forms.Form):
    amount = forms.CharField(label='amount to pay', max_length=100)
    name = forms.CharField(label='Your full name', max_length=100)
    email = forms.CharField(label='Your email  adress', max_length=100)