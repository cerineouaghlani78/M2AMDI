from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def option1(request):
    return render(request, 'option1.html')

def option2(request):
    return render(request, 'option2.html')

def menu(request):
    return render(request, 'menu.html')

def logout(request):
    return render(request, 'logout.html')