from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Company
from django.contrib.auth.mixins import LoginRequiredMixin

class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'companies/company_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Companies'
        context['headers'] = ['ID', 'Name', 'Contact', 'Headquarters']
        context['create_url'] = reverse_lazy('company_create')
        context['update_url_name'] = 'company_update'
        context['delete_url_name'] = 'company_delete'
        return context

class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('company_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Company'
        context['cancel_url'] = self.success_url
        return context

class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('company_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Company: {self.object.name}'
        context['cancel_url'] = self.success_url
        return context

class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('company_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context
