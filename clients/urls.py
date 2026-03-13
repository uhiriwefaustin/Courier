from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.ClientListView.as_view(), name='client_list'),
    path('clients/create/', views.ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/update/', views.ClientUpdateView.as_view(), name='client_update'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client_delete'),
    
    path('receivers/', views.ReceiverListView.as_view(), name='receiver_list'),
    path('receivers/create/', views.ReceiverCreateView.as_view(), name='receiver_create'),
    path('receivers/<int:pk>/update/', views.ReceiverUpdateView.as_view(), name='receiver_update'),
    path('receivers/<int:pk>/delete/', views.ReceiverDeleteView.as_view(), name='receiver_delete'),
]
