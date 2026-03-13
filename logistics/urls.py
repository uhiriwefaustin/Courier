from django.urls import path
from . import views

urlpatterns = [
    # Routes
    path('routes/', views.BusRouteListView.as_view(), name='route_list'),
    path('routes/create/', views.BusRouteCreateView.as_view(), name='route_create'),
    path('routes/<int:pk>/update/', views.BusRouteUpdateView.as_view(), name='route_update'),
    path('routes/<int:pk>/delete/', views.BusRouteDeleteView.as_view(), name='route_delete'),
    
    # Stations
    path('stations/', views.StationListView.as_view(), name='station_list'),
    path('stations/create/', views.StationCreateView.as_view(), name='station_create'),
    path('stations/<int:pk>/update/', views.StationUpdateView.as_view(), name='station_update'),
    path('stations/<int:pk>/delete/', views.StationDeleteView.as_view(), name='station_delete'),
    
    # Drivers
    path('drivers/', views.DriverListView.as_view(), name='driver_list'),
    path('drivers/create/', views.DriverCreateView.as_view(), name='driver_create'),
    path('drivers/<int:pk>/update/', views.DriverUpdateView.as_view(), name='driver_update'),
    path('drivers/<int:pk>/delete/', views.DriverDeleteView.as_view(), name='driver_delete'),
]
