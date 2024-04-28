# users/urls.py

from django.urls import path
from .views import UserRegistrationView, UserLoginView
from django.views.generic import TemplateView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('', TemplateView.as_view(template_name='users/index.html'), name='user_index'),
]
