from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class MenuView(LoginRequiredMixin, View):
    template_name = 'DatingSite/menu.html'

    def get(self, request):
        return render(request, self.template_name)
