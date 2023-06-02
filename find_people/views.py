from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from user_profile.models import UserInfo
from .filters import UserFilter


class ListPeopleView(LoginRequiredMixin, View):
    template_name = 'find_people/list_profiles.html'

    def get(self, request):
        profiles_for_watching = UserInfo.objects.all()
        annotated_users = UserInfo.user_liked(request.user.pk, profiles_for_watching)
        print(annotated_users.filter(liked=True))
        return render(request, self.template_name, context={'profiles_list': annotated_users})

    def post(self, request):
        liked_user = UserInfo.objects.get(login=int(request.POST['liked_user']))
        current_user = UserInfo.objects.get(login=request.user.pk)
        current_user.liked_users.add(liked_user)
        current_user.save()
        print((current_user.name, current_user.liked_users.all()))
        return redirect('/accounts/people')


class SearchView(View):
    def get(self, request):
        user_list = UserInfo.objects.all()
        user_filter = UserFilter(request.GET, queryset=user_list)
        return render(request, 'find_people/search_users.html', {'filter': user_filter})

