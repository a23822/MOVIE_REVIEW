from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model
from .models import User
from movies.models import Score
from .forms import UserCustomCreationForm


def index(request):
    users = User.objects.all()
    return render(request, 'accounts/list.html', {
        'users':users,
    })
    
def detail(request, user_id):
    profile = get_object_or_404(get_user_model(), pk=user_id)
    #recomm = Score.objects.filter(user_id__in=profile.user_followers_user.values('id')).order_by('value')
    #recomm = profile.user_followers_user.all()
    recomm = Score.objects.filter(user_id__in=profile.user_followings_user.values('id'))
    ref = profile.user_followings_user.values_list('pk', 'username')
    refs = []
    for r in ref:
        recom = Score.objects.filter(user_id=r[0]).order_by('-value')[0]
        refs.append(recom)
    # refs = list
    # for r in refs:
    #     recom = Score.objects.filter(user_id__in=r).order_by('value')
    #     print(recom)
    
    return render(request, 'accounts/detail.html', {
        'profile' : profile,
        'recomm' : recomm,
        'refs' : refs,
    })

@login_required
def follow(request, user_id, follower_id):
    print(follower_id)
    following = get_object_or_404(get_user_model(), pk=user_id)
    follower = get_object_or_404(get_user_model(), pk=follower_id)
    #언팔로우
    if request.user in following.user_followers_user.all():
        following.user_followers_user.remove(request.user)
        follower.user_followings_user.remove(following)
    #팔로우
    else:
        following.user_followers_user.add(request.user)
        follower.user_followings_user.add(following)
    
    return redirect('accounts:detail', following.pk)

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
