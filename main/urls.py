"""
URL configuration for the main app.
"""
from django.urls import path
from .views import PortfolioView

app_name = 'main'

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
]
