from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from datetime import datetime

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/index.html'
    extra_context = {'today': datetime.today()}


class LoginView(LoginView):
    template_name='home/login.html'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('note.list')
        return super().get(request, *args, **kwargs)


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name='home/logout.html'


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name='home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('note.list')
        return super().get(request, *args, **kwargs)