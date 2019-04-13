from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'leads/leads.html')

def noncontact(request):
    return render(request, 'leads/noncontact.html')

def followup(request):
    return render(request, 'leads/followup.html')

def walkin(request):
    return render(request, 'leads/walkin.html')