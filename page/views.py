
from django.shortcuts import render
# Create your views here.

def dashboard(request):
    return render(request, 'page/dashboard.html', {'title': 'Dashboard'})

def sales(request):
    return render(request, 'page/sales.html', {'title': 'My Sales'})

def search(request):
    return render(request, 'page/search.html', {'title': 'Property Search'})

def reports(request):
    return render(request, 'page/reports.html', {'title': 'Reports'})

def listing(request):
    return render(request, 'page/listing.html', {'title': 'Manage Property Listing'})

def management(request):
    return render(request, 'page/management.html', {'title': 'Account Management'})


 