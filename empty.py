from django.urls import path
from . import views

urlpatterns = [
    path('tracking/', include('tracking.urls')),
    path('payments/', include('payments.urls')),
    path('audit/', include('audit.urls')),
]
