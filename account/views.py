from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def _login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('articles:list')
        return render(request, 'auth/user404.html')
    return render(request, 'auth/login.html')


def login_view(request):
    if not request.user.is_anonymous:
        return redirect('articles:list')
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_path = request.GET.get('next')
            if next_path:
                return redirect(next_path)
            return redirect('articles:list')
    ctx = {
        'form':form
    }
    return render(request, 'auth/login.html', ctx)


def logout_view(request):
    if not request.user.is_anonymous:
        if request.method == 'POST':
            logout(request)
            return redirect('auth:login')
    else:
        return redirect('auth:login')
    return render(request, 'auth/logout.html')

def register_view(request):
    if not request.user.is_authenticated:
        return redirect('articles:list')
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('auth:login')
    contex = {
        'form': form
    }
    return render(request, 'auth/register.html', contex)