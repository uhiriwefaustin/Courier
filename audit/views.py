from django.urls import reverse_lazy
from django.views.generic import ListView
from .models import AuditLog
from django.contrib.auth.mixins import LoginRequiredMixin

class AuditLogListView(LoginRequiredMixin, ListView):
    model = AuditLog
    template_name = 'audit/audit_list.html'
    ordering = ['-timestamp']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'System Audit Logs'
        context['headers'] = ['Log ID', 'Table', 'Record ID', 'Action', 'User', 'Time']
        return context
