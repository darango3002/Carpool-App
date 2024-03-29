from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Ride, Car
from .forms import RideForm, CarForm
from address.models import Address
from django.conf import settings

def home(request):
    context = {
        'rides': Ride.objects.all()
    }
    return render(request, 'ride_finder/home.html', context)

class RideListView(ListView):
    model = Ride
    template_name = 'ride_finder/home.html'
    context_object_name = 'rides'
    ordering = ['-date_posted']

class RideDetailView(DetailView):
    model = Ride

class RideCreateView(LoginRequiredMixin, CreateView):
    model = Ride
    form_class = RideForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(request=self.request, message="Ride Successfully Created!")
        return super().form_valid(form)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RideCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_api_key'] = settings.GOOGLE_API_KEY
        context['base_country'] = settings.BASE_COUNTRY
        return context

        
class RideUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Ride
    form_class = RideForm
    template_name_suffix = "_update_form"

    def form_valid(self, form):
        form.instance.creator = self.request.user
        messages.success(request=self.request, message="Ride Successfully Updated!")
        return super().form_valid(form)

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(RideUpdateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['user'] = self.request.user
        return kwargs

    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.creator:
            return True
        return False

class RideDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Ride
    success_url = '/'
    
    def test_func(self):
        ride = self.get_object()
        if self.request.user == ride.creator:
            return True
        return False
    
class CarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarForm
    success_url = "/ride/new/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        
def about(request):
    return render(request, 'ride_finder/about.html')
