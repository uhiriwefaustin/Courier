from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('accounts/', include('accounts.urls')),
    path('clients/', include('clients.urls')),
    path('packages/', include('packages.urls')),
    path('companies/', include('companies.urls')),
    path('logistics/', include('logistics.urls')),
    path('tracking/', include('tracking.urls')),
    path('payments/', include('payments.urls')),
    path('audit/', include('audit.urls')),
]
