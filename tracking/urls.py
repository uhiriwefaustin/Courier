from django.urls import path
from . import views

urlpatterns = [
    # Tracking
    path('updates/', views.TrackingListView.as_view(), name='tracking_list'),
    path('updates/create/', views.TrackingCreateView.as_view(), name='tracking_create'),
    path('updates/<int:pk>/update/', views.TrackingUpdateView.as_view(), name='tracking_update'),
    path('updates/<int:pk>/delete/', views.TrackingDeleteView.as_view(), name='tracking_delete'),
    
    # Exceptions
    path('exceptions/', views.ExceptionListView.as_view(), name='exception_list'),
    path('exceptions/create/', views.ExceptionCreateView.as_view(), name='exception_create'),
    path('exceptions/<int:pk>/update/', views.ExceptionUpdateView.as_view(), name='exception_update'),
    path('exceptions/<int:pk>/delete/', views.ExceptionDeleteView.as_view(), name='exception_delete'),
]
