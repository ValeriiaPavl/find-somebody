from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import UserDescription
from .image_processing import save_avatar
from .models import UserInfo


class CreateProfileView(LoginRequiredMixin, View):
    template_name = 'user_profile/edit_profile.html'
    form_class = UserDescription

    def get(self, request):
        return render(request, self.template_name, context={'form': self.form_class()})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user_description = form.save(commit=False)
            user_description.login = request.user
            user_description.user_avatar = save_avatar(user_description.login.username, request.FILES['avatar'])
            user_description.save()
            return redirect('user_profile:view_profile', user=request.user)
        else:
            return HttpResponse("File didn't upload")


class EditProfileView(LoginRequiredMixin, View):
    form_class = UserDescription
    #
    # def get_test_func(self):
    #     login = self.request.user.pk

    def get(self, request, login_id):
        profile = get_object_or_404(UserInfo, login=login_id)
        form = self.form_class(instance=profile)
        return render(request, 'user_profile/edit_profile.html', {'form': form})

    def post(self, request, login_id=None):
        if login_id is None:
            login_id = request.user.pk
        profile = UserInfo.objects.get(login=login_id)
        form = self.form_class(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user_description = form.save(commit=False)
            user_description.login = request.user
            user_description.user_avatar = save_avatar(user_description.login.username, request.FILES['avatar'])
            user_description.save()
            return redirect('user_profile:view_profile', login_id=login_id)
        else:
            return HttpResponse("Your form is bad")


class ViewProfileView(LoginRequiredMixin, View):
    template_name = 'user_profile/view_profile.html'


    def get(self, request, login_id=None):
        if login_id is None:
            login_id = request.user.pk
        try:
            user_info = UserInfo.objects.get(login=login_id)
        except Http404:
            return redirect('user_profile:create_profile')
        user_likes = user_info.liked_users.all()
        context = {'user_info': user_info, 'user_likes': user_likes}
        return render(request, self.template_name, context)









