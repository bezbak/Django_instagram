from django.shortcuts import render, redirect
from users.models import User, Follows
from django.contrib.auth import authenticate, login
# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        profile_image = request.FILES.get('profile_image')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password:
            user = User.objects.create(username = username, email= email, phone = phone, profile_image = profile_image)
            user.set_password(password)
            user.save()
            user = User.objects.get(username = username)
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('index')
    return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.get(username = username)
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('index')
    
    return render(request, 'sign-in.html')

def account(request, id):
    user = User.objects.get(id = id)
    follow_status = Follows.objects.filter(from_user = request.user, to_user = user).exists()
    if request.method == 'POST':
        if 'follow' in request.POST:
            try:
                follow = Follows.objects.get(from_user = request.user, to_user = user)
                follow.delete()
                return redirect('account', user.id)
            except:
                follow = Follows.objects.create(from_user = request.user, to_user = user)
                follow.save()
                return redirect('account', user.id)
    context = { 
        'user': user,
        'follow_status':follow_status,
    }
    return render(request, 'my_account.html', context)

def edit_profile(request, id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        username = request.POST.get('username')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        description = request.POST.get('description')
        profile_image = request.FILES.get('profile_image')
        try:
            user = User.objects.get(id = id)
            user.username = username 
            user.phone = phone 
            user.email = email
            user.description = description
            user.profile_image = profile_image
            user.save()
            return redirect('account', user.id)
        except:
            return redirect('edit_profile', user.id)
    return render(request, 'edit_profile.html')

def followers(request, id):
    user = User.objects.get(id = id)
    if request.method == "POST":
        if 'delete' in request.POST:
            follower = request.POST.get('follower')
            follow_status = Follows.objects.all().filter(from_user_id = follower, to_user = user)
            follow_status.delete()
            return redirect('followers', user.id)
    context = {
        'user':user
    }
    return render(request, 'followers.html', context)

def follows(request, id):
    user = User.objects.get(id = id)
    if request.method == 'POST':
        follow = request.POST.get('follow')
        follow_status = Follows.objects.all().filter(from_user = user, to_user_id = follow)
        follow_status.delete()
    context = {
        'user':user
    }
    return render(request, 'follows.html', context)