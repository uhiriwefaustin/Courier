from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import BusRoute, Station, Driver
from django.contrib.auth.mixins import LoginRequiredMixin

# BusRoute CRUD
class BusRouteListView(LoginRequiredMixin, ListView):
    model = BusRoute
    template_name = 'logistics/busroute_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bus Routes'
        context['headers'] = ['ID', 'Company', 'From', 'To', 'Duration', 'Frequency']
        context['create_url'] = reverse_lazy('route_create')
        context['update_url_name'] = 'route_update'
        context['delete_url_name'] = 'route_delete'
        return context

class BusRouteCreateView(LoginRequiredMixin, CreateView):
    model = BusRoute
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('route_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Route'
        context['cancel_url'] = self.success_url
        return context

class BusRouteUpdateView(LoginRequiredMixin, UpdateView):
    model = BusRoute
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('route_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Route: {self.object}'
        context['cancel_url'] = self.success_url
        return context

class BusRouteDeleteView(LoginRequiredMixin, DeleteView):
    model = BusRoute
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('route_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context

# Station CRUD
class StationListView(LoginRequiredMixin, ListView):
    model = Station
    template_name = 'logistics/station_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Stations'
        context['headers'] = ['ID', 'Route', 'Station Name', 'City']
        context['create_url'] = reverse_lazy('station_create')
        context['update_url_name'] = 'station_update'
        context['delete_url_name'] = 'station_delete'
        return context

class StationCreateView(LoginRequiredMixin, CreateView):
    model = Station
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('station_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Station'
        context['cancel_url'] = self.success_url
        return context

class StationUpdateView(LoginRequiredMixin, UpdateView):
    model = Station
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('station_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Station: {self.object.station_name}'
        context['cancel_url'] = self.success_url
        return context

class StationDeleteView(LoginRequiredMixin, DeleteView):
    model = Station
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('station_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context

# Driver CRUD
class DriverListView(LoginRequiredMixin, ListView):
    model = Driver
    template_name = 'logistics/driver_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Drivers'
        context['headers'] = ['ID', 'Name', 'Phone', 'Vehicle', 'Company']
        context['create_url'] = reverse_lazy('driver_create')
        context['update_url_name'] = 'driver_update'
        context['delete_url_name'] = 'driver_delete'
        return context

class DriverCreateView(LoginRequiredMixin, CreateView):
    model = Driver
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('driver_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Driver'
        context['cancel_url'] = self.success_url
        return context

class DriverUpdateView(LoginRequiredMixin, UpdateView):
    model = Driver
    fields = '__all__'
    template_name = 'crud/form.html'
    success_url = reverse_lazy('driver_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Update Driver: {self.object.name}'
        context['cancel_url'] = self.success_url
        return context

class DriverDeleteView(LoginRequiredMixin, DeleteView):
    model = Driver
    template_name = 'crud/confirm_delete.html'
    success_url = reverse_lazy('driver_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cancel_url'] = self.success_url
        return context
