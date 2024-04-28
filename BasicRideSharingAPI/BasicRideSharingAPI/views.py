# views.py
from django.shortcuts import render

def home(request):
    # Pass any necessary data to the template, such as URLs of different apps
    app_urls = {
        'user_api': '/users/',
        'ride_api': '/rides/',
        # Add more app URLs as needed
    }
    return render(request, 'home.html', {'app_urls': app_urls})