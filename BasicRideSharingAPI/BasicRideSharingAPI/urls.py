# BasicRideSharingAPI/urls.py
from django.contrib import admin
from django.urls import path, include
from .views import home
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls,name='admin-site-urls'),
    path('users/', include('users.urls')),  # Include your users API URLs here
    path('rides/', include('rides.urls')),  # Include Ride API URLs here
    path('', home, name='home'),
]
