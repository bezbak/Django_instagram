from django.shortcuts import render, redirect
from posts.models import Post
from users.models import User
# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)

def single_post(request, id):
    post = Post.objects.get(id = id)
    context = {
        'post':post
    }
    return render(request, 'comment.html', context)

def create_post(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        user = request.user
        post = Post.objects.create(title = title, description = description, image = image, user = user)
        post.save()
        return redirect('index')
    return render(request, 'create_post.html')

def update_post(request,id):
    user = request.user
    post = Post.objects.get(id = id)
    if user == post.user:
        if request.method == "POST":
            title = request.POST.get('title')
            description = request.POST.get('description')
            image = request.FILES.get('image')
            post.title = title
            post.description = description
            post.image = image
            post.user = user
            post.save()
            return redirect('index')
    else:
        return redirect('index')
    return render(request, 'update_post.html')