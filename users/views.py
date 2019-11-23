from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def register(request):
    
    if request.method == 'POST':
        registration_form = UserCreationForm(request.POST)
        if registration_form.is_valid():
            username = forn.cleaned_data.get('username')
    else:
        registration_form = UserCreationForm()
    
    
    return render(request, 'users/register.html', { 'form': registration_form })
