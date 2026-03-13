from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')


class DashboardView(LoginRequiredMixin, TemplateView):

    def get_template_names(self):
        user = self.request.user
        if user.is_superuser or user.role == 'Admin':
            return ['dashboard/admin_dashboard.html']
        elif user.role == 'Manager':
            return ['dashboard/manager_dashboard.html']
        elif user.role == 'Clerk':
            return ['dashboard/clerk_dashboard.html']
        elif user.role == 'Driver':
            return ['dashboard/driver_dashboard.html']
        elif user.role == 'Auditor':
            return ['dashboard/auditor_dashboard.html']
        else:
            return ['dashboard/default_dashboard.html']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        # Lazy imports to avoid circular dependencies
        from companies.models import Company
        from packages.models import Package
        from payments.models import Payment
        from logistics.models import Driver, BusRoute, Station
        from clients.models import Client, Receiver
        from tracking.models import Tracking, PackageException
        from audit.models import AuditLog
        from accounts.models import User

        if user.is_superuser or user.role == 'Admin':
            context['total_companies'] = Company.objects.count()
            context['total_packages'] = Package.objects.count()
            context['total_users'] = User.objects.count()
            context['total_audit_logs'] = AuditLog.objects.count()
            context['in_transit'] = Package.objects.filter(status='In Transit').count()
            context['delivered'] = Package.objects.filter(status='Delivered').count()
            context['pending'] = Package.objects.filter(status='Pending').count()
            context['exceptions'] = Package.objects.filter(status='Exception').count()

        elif user.role == 'Manager':
            context['total_routes'] = BusRoute.objects.count()
            context['total_drivers'] = Driver.objects.count()
            context['in_transit'] = Package.objects.filter(status='In Transit').count()
            context['total_exceptions'] = PackageException.objects.count()

        elif user.role == 'Clerk':
            context['total_clients'] = Client.objects.count()
            context['packages_today'] = Package.objects.count()
            from django.db.models import Sum
            total_payments = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
            context['total_payments'] = total_payments

        elif user.role == 'Driver':
            context['assigned_packages'] = Package.objects.filter(
                driver__name=user.username, status='In Transit'
            ).count()
            context['delivered_today'] = Package.objects.filter(
                driver__name=user.username, status='Delivered'
            ).count()

        elif user.role == 'Auditor':
            context['total_audit_logs'] = AuditLog.objects.count()
            from django.db.models import Sum
            context['total_payments_amount'] = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
            context['total_packages'] = Package.objects.count()
            context['delivered_packages'] = Package.objects.filter(status='Delivered').count()
            context['recent_payments'] = Payment.objects.select_related('package').all().order_by('-payment_date')[:5]

        return context
