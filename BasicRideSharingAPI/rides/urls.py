from django.urls import path
from django.views.generic import TemplateView
from .views import RideDetailsByIdListView, RidesFullDetailsView, RideCreateAPIView,UpdateRideStatusAPIView

urlpatterns = [
    path('', TemplateView.as_view(template_name='rides/index.html'), name='rides_index'),
    path('create/', RideCreateAPIView.as_view(), name='ride_create'),
    path('view/', RideDetailsByIdListView.as_view(), name='ride_list'),
    path('view_all/', RidesFullDetailsView.as_view(), name='ride_list_all'),
    path('update-status/', UpdateRideStatusAPIView.as_view(), name='update_ride_status'),
]
