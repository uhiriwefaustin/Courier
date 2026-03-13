from django.urls import path
from . import views

urlpatterns = [
    path('', views.PaymentListView.as_view(), name='payment_list'),
    path('create/', views.PaymentCreateView.as_view(), name='payment_create'),
    path('<int:pk>/update/', views.PaymentUpdateView.as_view(), name='payment_update'),
    path('<int:pk>/delete/', views.PaymentDeleteView.as_view(), name='payment_delete'),
]
