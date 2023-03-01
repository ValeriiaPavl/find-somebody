from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from user_profile.models import UserInfo


class ListPeopleView(LoginRequiredMixin, View):
    template_name = 'find_people/list_profiles.html'

    def get(self, request):
        return render(request, self.template_name, context={'profiles_list': UserInfo.objects.all()})

