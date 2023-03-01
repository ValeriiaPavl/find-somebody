from django.urls import path
from .views import CreateProfileView, ViewProfileView, EditProfileView
from django.contrib.auth.views import LogoutView, LoginView

app_name = 'user_profile'
urlpatterns = [
    path('accounts/login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view()),
    path('accounts/profile/<int:login_id>', ViewProfileView.as_view(), name='view_profile'),
    path('accounts/profile/<int:login_id>/edit', EditProfileView.as_view(), name='edit_profile'),
    path('accounts/profile/edit/', CreateProfileView.as_view(), name='create_profile')
]