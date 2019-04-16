from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Telecaller

# Create your views here.

def candidate(request):
    if request.method == 'POST':
        # Add Data
        return
    else:
        return render(request, 'candidates/candidate.html')

def candidates(request):
    if request.method == 'POST':
        # Add Data
        return
    else:
        return render(request, 'candidates/candidates.html')

def addleads(request):
    if request.method == 'POST':
        # Add Data
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        qualification = request.POST['qualification']
        colname = request.POST['colname']
        address = request.POST['address']
        course = request.POST['course']
        remark = request.POST['remark']
        reason = request.POST['reason']

        telecaller = Telecaller(name=name, phone=phone, email=email, qualification=qualification, colname=colname, address=address, course=course, remark=remark, reason=reason)

        telecaller.save()
        return redirect('teleform')
    else:
        return render(request, 'candidates/telecallerform.html')

def enquiry(request):
    if request.method == 'POST':
        # Add Data
        return
    else:
        return render(request, 'candidates/enquiryform.html')

def admission(request):
    if request.method == 'POST':
        # Add Data
        return
    else:
        return render(request, 'candidates/admission.html')