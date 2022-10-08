from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib import messages

from .models import BlogPost, Profile
from .forms import BlogPostForm, ProfileForm

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password != confirm_password:
            messages.error(request, 'passwords do not match')
            return redirect('/register')

        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')
    return render(request, 'register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('/')
        else:
            messages.error(request, 'invalid credentials')
        return render('blog.html')
    return render(request, 'login.html')

def user_logout(request):
    logout(request=request)
    messages.success(request, 'successfully logged out')
    return redirect('/login')

# profile
def profile(request):
    return render(request, 'profile.html')

def user_profile(request, uid):
    post = BlogPost.objects.filter(id=uid)
    return render(request, 'user_profile.html', { 'post': post })

def edit_user_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, 'edit_profile.html', { 'alert': alert })
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', { 'form': form })

# blogs - CURD
def blogs(request):
    posts = BlogPost.objects.filter().order_by('-created_on')
    return render(request, 'blog.html', { 'posts': posts })

def blog_detail(request, slug):
    post = BlogPost.objects.get(slug=slug)
    return render(request, "blog_detail.html", { 'post':post })

@login_required(login_url='/login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            obj = form.instance
            alert = True
            return render(request, 'add_blog.html', { 'obj': obj, 'alert': alert })
    else:
        form = BlogPostForm()
    return render(request, 'add_blog.html', { 'form': form })

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name: str = 'edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'image']

def delete_blog_post(request, slug):
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', { 'posts': post })

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        blogs = BlogPost.objects.filter(title__contains=searched)
        return render(request, 'search.html', { 'searched': searched, 'blogs': blogs })
    else:
        return render(request, 'search.html', {})
