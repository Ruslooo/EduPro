
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
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
        return context

    def form_valid(self, form):
        if not form.is_valid():
            return render(self.request, self.template_name, {"errors": form.errors})

        form.save()
        username, password = form.cleaned_data.get("username"), form.cleaned_data.get("password1")
        account = authenticate(self.request, username=username, password=password)
        login(self.request, account)
        return redirect('common:home')



class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'profiles/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('common:home')


def logout_user(request):
    logout(request)
    return redirect('profiles:login')


def profile(request):
    profiles = Profile.objects.all()
    context = {
        'profiles': profiles

    }
    return render(request, 'profiles/profile.html', context=context)