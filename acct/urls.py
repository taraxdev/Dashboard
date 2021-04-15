from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('products/',views.product),
    path('customer/',views.customer),
    path('dashboard/',views.dashboard),
]
