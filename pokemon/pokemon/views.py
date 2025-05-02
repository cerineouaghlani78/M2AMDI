from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('pokedex')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def option1(request):
    return render(request, 'option1.html')

def option2(request):
    return render(request, 'option2.html')

def menu(request):
    return render(request, 'menu.html')

def logout_view(request):
    logout(request)
    return redirect('login.html')

@login_required
def pokedex_view(request):
    return render(request, 'pokedex.html')