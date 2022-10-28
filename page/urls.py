from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name = 'page-dashboard'),
    path('sales/', views.sales, name = 'page-sales'),
    path('search/', views.search, name = 'page-search'),
    path('reports/', views.reports, name = 'page-reports'),
    path('listing/', views.listing, name = 'page-listing'),
    path('management/', views.management, name = 'page-management'),
]