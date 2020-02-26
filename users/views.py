from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import SignUpForm, CustomUserUpdateForm


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST': 
        form = CustomUserUpdateForm(request.POST, instance=user, files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = CustomUserUpdateForm(instance=user)

    return render(request, 'users/profile.html', {'form': form})