from django.shortcuts import render
from django.views.generic import CreateView,FormView,UpdateView,DetailView,ListView
from .forms import UserRegisterForm,UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect
from .models import Account
# Create your views here.


class RegisterView(FormView):
    template_name='accounts/register.html'
    form_class=UserRegisterForm
    success_url=reverse_lazy('profile')

    def form_valid(self,form):
        user=form.save()
        login(self.request, user)
        
        return super().form_valid(form)

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

class ChangeUserForm(LoginRequiredMixin,UpdateView):
    template_name='accounts/user_change.html'
    form_class=UserUpdateForm
    success_url=reverse_lazy('profile')
    
    def get_object(self):
            return self.request.user


class UserLoginView(LoginView):
    template_name='accounts/Login.html'
    next_page='profile'

    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('profile')
        return super().dispatch(request, *args, **kwargs)

class ProfileView(LoginRequiredMixin,DetailView):
    model=Account
    template_name='accounts/profile.html'
    context_object_name='account'
    
    def get_object(self):
        account, _ = Account.objects.get_or_create(
            user=self.request.user,
            defaults={
                'date_of_birth': None,
                'phone': '',
                'address': '',
            }
        )
        return account
