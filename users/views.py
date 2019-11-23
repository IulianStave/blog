from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# Create your views here.

def register(request):
    
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Account created for user {username}')
            return redirect('blog-home')
    else:
        registration_form = UserCreationForm()
    
    
    return render(request, 'users/register.html', { 'form': registration_form })
