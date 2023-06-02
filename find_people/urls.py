from django.urls import path
from .views import ListPeopleView, SearchView

urlpatterns = [
    path("accounts/people", ListPeopleView.as_view()),
    path("accounts/people/search", SearchView.as_view()),
]