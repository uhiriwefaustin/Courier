from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Client, Receiver
from django.contrib.auth.mixins import LoginRequiredMixin

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'clients/client_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Clients'
        context['headers'] = ['ID', 'Name', 'Phone', 'Email']
        context['create_url'] = reverse_lazy('client_create')
        context['update_url_name'] = 'client_update'
        context['delete_url_name'] = 'client_delete'
        return context

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('client_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Client'
        context['cancel_url'] = self.success_url
        return context

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('client_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Client: {self.object.name}'
        context['cancel_url'] = self.success_url
        return context

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('client_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context

# Receiver Views
class ReceiverListView(LoginRequiredMixin, ListView):
    model = Receiver
    template_name = 'clients/receiver_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Receivers'
        context['headers'] = ['ID', 'Name', 'Phone', 'Address']
        context['create_url'] = reverse_lazy('receiver_create')
        context['update_url_name'] = 'receiver_update'
        context['delete_url_name'] = 'receiver_delete'
        return context

class ReceiverCreateView(LoginRequiredMixin, CreateView):
    model = Receiver
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('receiver_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Receiver'
        context['cancel_url'] = self.success_url
        return context

class ReceiverUpdateView(LoginRequiredMixin, UpdateView):
    model = Receiver
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('receiver_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Receiver: {self.object.name}'
        context['cancel_url'] = self.success_url
        return context

class ReceiverDeleteView(LoginRequiredMixin, DeleteView):
    model = Receiver
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('receiver_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context
