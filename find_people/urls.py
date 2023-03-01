from django.urls import path
from .views import ListPeopleView

urlpatterns = [
    path("accounts/people", ListPeopleView.as_view())
]