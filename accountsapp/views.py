from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.

def signup(request):
    if request.method == 'GET':
        form = SignUpForm()
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, 'Form submission successful')
        else:
            messages.error(request, 'Form submission is not successful')
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.warning(request, 'User is not active')
                return redirect('index')
        else:
            messages.error(request, 'User not found')
            return redirect('index')
       