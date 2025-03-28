from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/customers/')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/customers/')
    else:
        form = SignUpForm()
    return render(request, 'accounts/sign_up.html',{'form':form})

from django.contrib.sessions.models import Session
from django.shortcuts import render
from django.utils import timezone

def session_list(request):
    # セッション情報を全て取得
    sessions = Session.objects.all()

    # セッションデータをユーザー名とセッション開始時間に変換
    session_data = []
    for session in sessions:
        session_info = {
            'session_key': session.session_key,
            'user_id': session.get_decoded().get('_auth_user_id', '未ログイン'),
            'last_activity': timezone.localtime(session.get_decoded().get('_auth_user_last_login', timezone.now()))
        }
        session_data.append(session_info)

    return render(request, 'accounts/session_list.html', {'sessions': session_data})
