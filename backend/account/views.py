from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
logger = logging.getLogger(__name__)


@login_required
def dashboard(request):
    """
    Функция для отображения дашборда.
    """
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


@csrf_exempt
def register(request):
    """
    Функция для регистрации пользователя.
    """
    if request.method == 'POST':
        data = json.loads(request.body) # Использование JSON
        logger.debug(data)
        user_form = UserRegistrationForm(data)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return JsonResponse({'status': 'success'}, status=200) # Использование JSON
        else:
            return JsonResponse({'errors': user_form.errors}, status=400) # Использование JSON
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405) # Использование JSON


def user_login(request):
    """
    Функция для входа пользователя.
    """
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def edit(request):
    """
    Функция для редактирования профиля пользователя.
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})



