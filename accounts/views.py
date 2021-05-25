from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout, authenticate
from .forms import SignupForm

def login_view(request):
    form=AuthenticationForm()
    #폼에 저장해주고
    return render(request, 'login.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username=username, password=password)
            #authenticate는 인증된 사용자인지
            if user is not None:
                login(request, user)
                return redirect('home')
    else: #포스트로 들어오지 않은 경우에는 폼을 띄워주면 된다
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
	logout(request)
	return redirect('home')

def signup_view(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form':form})
    #모든 경우에 return이 있어야 하니깐 인덴트를 여길로 설정해주기
    #signup.html로 폼을 보낸 것

# Create your views here.
