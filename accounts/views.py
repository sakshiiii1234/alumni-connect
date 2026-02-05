from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import RegisterForm
from .models import User

def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_approved = False   # wait for teacher approval
            user.save()

            messages.success(request, "Account created! Wait for teacher approval.")
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            if not user.is_approved:
                messages.error(request, "Your account is not approved yet.")
                return redirect('login')

            login(request, user)

            # 🔁 Redirect after login
            return redirect('dashboard')

        else:
            messages.error(request, "Invalid credentials")

    return render(request, 'login.html')


