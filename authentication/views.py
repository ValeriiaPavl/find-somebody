from django.http import HttpResponse
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm
from django.views import View


class SignUpView(View):
    form_class = RegistrationForm

    def get(self, request):
        return render(request, 'registration/signup.html', {"form": self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        return HttpResponse("Your form is bad")

