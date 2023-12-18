from django.urls import path
from . import views
from .views import (
    RideListView,
    RideDetailView,
    RideCreateView,
    RideUpdateView,
    RideDeleteView,
    CarCreateView
)

urlpatterns = [
    path('', RideListView.as_view(), name='ridefinder-home'),
    path('ride/<int:pk>/', RideDetailView.as_view(), name='ride-detail'),
    path('ride/new/', RideCreateView.as_view(), name='ride-create'),
    path('ride/<int:pk>/update', RideUpdateView.as_view(), name='ride-update'),
    path('ride/<int:pk>/delete', RideDeleteView.as_view(), name='ride-delete'),
    path('car/new/', CarCreateView.as_view(), name='car-create'),
    path('about/', views.about, name='ridefinder-about')
]