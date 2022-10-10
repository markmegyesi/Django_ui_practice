from multiprocessing import context
from django.shortcuts import render,redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import ProfileModel
from django.contrib.auth.models import User

def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            usr_obj = User.objects.filter(username=username).first()
            prof_temp = ProfileModel.objects.create(user_id=usr_obj.pk)

            messages.success(request, f" Your account has been created! You're able to log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
        }
    return render(request, 'user/register.html', context=context)

#@login_required(login_url='login')

def profile_view(request):
    return render(request, 'user/profile.html')
   