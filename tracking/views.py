from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Tracking, PackageException
from django.contrib.auth.mixins import LoginRequiredMixin

# Tracking CRUD
class TrackingListView(LoginRequiredMixin, ListView):
    model = Tracking
    template_name = 'tracking/tracking_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tracking Updates'
        context['headers'] = ['ID', 'Package', 'Station', 'Location', 'Status Update', 'Time']
        context['create_url'] = reverse_lazy('tracking_create')
        context['update_url_name'] = 'tracking_update'
        context['delete_url_name'] = 'tracking_delete'
        return context

class TrackingCreateView(LoginRequiredMixin, CreateView):
    model = Tracking
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('tracking_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Tracking Update'
        context['cancel_url'] = self.success_url
        return context

class TrackingUpdateView(LoginRequiredMixin, UpdateView):
    model = Tracking
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('tracking_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Tracking #{self.object.tracking_id}'
        context['cancel_url'] = self.success_url
        return context

class TrackingDeleteView(LoginRequiredMixin, DeleteView):
    model = Tracking
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('tracking_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context

# PackageException CRUD
class ExceptionListView(LoginRequiredMixin, ListView):
    model = PackageException
    template_name = 'tracking/exception_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Package Exceptions'
        context['headers'] = ['ID', 'Package', 'Type', 'Date Reported']
        context['create_url'] = reverse_lazy('exception_create')
        context['update_url_name'] = 'exception_update'
        context['delete_url_name'] = 'exception_delete'
        return context

class ExceptionCreateView(LoginRequiredMixin, CreateView):
    model = PackageException
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('exception_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Report Exception'
        context['cancel_url'] = self.success_url
        return context

class ExceptionUpdateView(LoginRequiredMixin, UpdateView):
    model = PackageException
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('exception_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Exception #{self.object.exception_id}'
        context['cancel_url'] = self.success_url
        return context

class ExceptionDeleteView(LoginRequiredMixin, DeleteView):
    model = PackageException
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('exception_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context
