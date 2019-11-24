from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.

def register(request):
    
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now login')
            return redirect('login')
    else:
        registration_form = UserRegistrationForm()
    
    
    return render(request, 'users/register.html', { 'form': registration_form })