from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions_details),
    path('<int:points>/', views.spend_points)
]