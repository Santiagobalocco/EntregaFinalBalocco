from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import ProfileForm, UserForm


from .models import Profile
from .forms import ProfileForm

@require_http_methods(["GET"])
def author_about(request, username):
    user = get_object_or_404(User, username=username)
    profile, _ = Profile.objects.get_or_create(user=user)
    return render(request, 'about.html', {'author': user, 'profile': profile})

@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})

from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.get_or_create(user=user)
            messages.success(request, "Usuario creado correctamente. Ahora puedes iniciar sesión.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


@login_required
@login_required
def profile_edit(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'accounts/profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def about(request):
    profile = request.user.profile
    return render(request, 'about.html', {'profile': profile})
