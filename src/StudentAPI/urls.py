from django.urls import path
from .views import overview as OverviewView

urlpatterns = [
    path('', OverviewView, name="overview"),
]