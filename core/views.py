from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

def certificate_pending(request):
    return render(request, 'core/certificate-pending.html')

def not_deployed_view(request):
    return render(request, 'core/not_deployed.html')