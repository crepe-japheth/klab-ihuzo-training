from django.shortcuts import render
from .forms import PaymentForm 
from .pay import make_payment 
from django.shortcuts import redirect

# Create your views here.

def index(request):
    form = PaymentForm()
    if request.method == 'POST':  # 1
        form = PaymentForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data['amount']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            
            return redirect(make_payment(amount,name,email))
           
    return render(request, 'flutter_wave/index.html', {'form':form})

  
