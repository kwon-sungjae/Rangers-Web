from django.shortcuts import render,redirect
from common.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request,user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html',{'form':form})

@login_required(login_url='/common/login/')
def mypage(request):
    user = request.user
    counting = user.counting/10
    return render(request, 'common/mypage.html', {'user':user,'counting':counting})

