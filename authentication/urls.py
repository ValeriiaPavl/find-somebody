from django.urls import path
from django.contrib.auth.views import LoginView
from .views import SignUpView

urlpatterns = [
    path('accounts/login/', LoginView.as_view()),
    path('signup', SignUpView.as_view())
]