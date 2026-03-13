from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Package
from django.contrib.auth.mixins import LoginRequiredMixin

class PackageListView(LoginRequiredMixin, ListView):
    model = Package
    template_name = 'packages/package_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Packages'
        context['headers'] = ['ID', 'Sender', 'Receiver', 'Driver', 'Status', 'Date Sent']
        context['create_url'] = reverse_lazy('package_create')
        context['update_url_name'] = 'package_update'
        context['delete_url_name'] = 'package_delete'
        return context

class PackageCreateView(LoginRequiredMixin, CreateView):
    model = Package
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('package_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create New Package'
        context['cancel_url'] = self.success_url
        return context

class PackageUpdateView(LoginRequiredMixin, UpdateView):
    model = Package
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('package_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Package: #{self.object.package_id}'
        context['cancel_url'] = self.success_url
        return context

class PackageDeleteView(LoginRequiredMixin, DeleteView):
    model = Package
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('package_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context
