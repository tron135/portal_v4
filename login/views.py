from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'login/login.html')

def logout(request):
    return redirect('login')