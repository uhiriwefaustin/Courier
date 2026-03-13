from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Payment
from django.contrib.auth.mixins import LoginRequiredMixin

class PaymentListView(LoginRequiredMixin, ListView):
    model = Payment
    template_name = 'payments/payment_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Payments'
        context['headers'] = ['ID', 'Package', 'Amount', 'Method', 'Date']
        context['create_url'] = reverse_lazy('payment_create')
        context['update_url_name'] = 'payment_update'
        context['delete_url_name'] = 'payment_delete'
        return context

class PaymentCreateView(LoginRequiredMixin, CreateView):
    model = Payment
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('payment_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Process Payment'
        context['cancel_url'] = self.success_url
        return context

class PaymentUpdateView(LoginRequiredMixin, UpdateView):
    model = Payment
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('payment_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Payment #{self.object.payment_id}'
        context['cancel_url'] = self.success_url
        return context

class PaymentDeleteView(LoginRequiredMixin, DeleteView):
    model = Payment
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('payment_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context
