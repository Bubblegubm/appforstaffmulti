from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


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


@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'status': 'Authenticated successfully'})
            else:
                return JsonResponse({'status': 'Disabled account'})
        else:
            return JsonResponse({'status': 'Invalid login'})

    else:
        return JsonResponse({'status': 'Invalid method'})


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



