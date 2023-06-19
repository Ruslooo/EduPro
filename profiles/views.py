
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import *

from common.models import *
from profiles.forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'profiles/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['institute'] = Institute.objects.all()
        context['department'] = Department.objects.all()
        context['title'] = 'Регистрация'
        return context

    def form_valid(self, form):
        if not form.is_valid():
            return render(self.request, self.template_name, {"errors": form.errors})

        user = form.save()
        user.follows.add(user)
        user.username, user.password = form.cleaned_data.get("username"), form.cleaned_data.get("password1")
        account = authenticate(self.request, username=user.username, password=user.password)
        login(self.request, account)
        return redirect('common:home')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'profiles/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вход'
        return context

    def get_success_url(self):
        return reverse_lazy('common:home')


def logout_user(request):
    logout(request)
    return redirect('profiles:login')


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profiles/profile_list.html", {"profiles": profiles})


def profile(request):
    user = request.user
    return render(request, 'profiles/profile.html', {'user': user})

