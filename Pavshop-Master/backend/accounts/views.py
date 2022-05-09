from email import message
from django.shortcuts import render,redirect
from .forms import RegistrationForm,LoginForm
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from accounts.tasks import send_confirmation_email
from django.utils.http import urlsafe_base64_decode
from accounts.tools.tokens import account_activation_token
from django.utils.encoding import force_str
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model, login as django_login, logout as django_logout
User = get_user_model()

def register(request):
    form = RegistrationForm()
    if request.method =='POST':
        form = RegistrationForm(data=request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password1'))
            user.is_active = False
            user.save()
            site_address = request.is_secure() and "https://" or "http://" + request.META['HTTP_HOST']  
            send_confirmation_email(user_id=user.id, site_address=site_address)
    context = {'form': form}
    return render(request, 'register.html', context)

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Email is activated')
        return redirect(reverse_lazy('index:home'))
    elif user:
        messages.error(request, 'Email is not activated.')
        return redirect(reverse_lazy('accounts:register'))
    else:
        messages.error(request, 'Email is already activated')
        return redirect(reverse_lazy('accounts:register'))
   

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user:
                django_login(request, user)
                messages.success(request, 'You logged in')
                return redirect(reverse_lazy('index:home'))
            messages.error(request, 'Your credentials are invalid')

    return render(request, 'login.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect(reverse_lazy('accounts:login'))