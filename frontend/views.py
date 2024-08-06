from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from recaptcha.forms import FormWithCaptcha
from registration.registration_user import registration_user
from authenticate.authenticate_user import authenticate_user
from user_posts.create_post import create_post as create_post_user
from user_posts.last_posts import last_posts
from logout.logout_user import logout_user
from user_extension.change_user_photo import change_user_photo
from posts.last_ten_posts import last_ten_posts
from django.contrib.auth.models import User
from django.http import HttpResponse
from posts.create_thread import create_thread
from posts.models import Post
from comments.models import Comment
from comments.create_comment import create_comment
from comments.get_comments import get_comments

def index(request):
    if request.method == 'GET':
        posts = last_ten_posts(request)
        update_posts = []

        for i in posts:
            user = User.objects.get(id=i.id_creator)
            update_posts.append({'photo': user.extension.photo, 'username': user.username, 'post': i})

        return render(request, 'frontend/html/index.html', context={'posts': update_posts})
    
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'frontend/html/login.html', context={'recaptcha': FormWithCaptcha})
        
        if request.method == 'POST':
            login = authenticate_user(request)
            if login == True:
                return HttpResponseRedirect('/')
            else:
                return render(request, 'frontend/html/login.html', context={'recaptcha': FormWithCaptcha, 'error': login['error']})
    else:
        return HttpResponseRedirect('/')
    
def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'frontend/html/registration.html', context={'recaptcha': FormWithCaptcha})
        
        if request.method == 'POST':
            reg = registration_user(request)
            if reg == True:
                return HttpResponseRedirect('/')
            else:
                return render(request, 'frontend/html/registration.html', context={'recaptcha': FormWithCaptcha, 'error': reg['error']})
    else:
        return HttpResponseRedirect('/')
    
def user(request, id):
    user = User.objects.filter(id=id)
    if user:
        posts = last_posts(id)
        if request.method == 'GET':
            return render(request, 'frontend/html/user.html', context={'user_profile': user[0], 'posts': posts})
        
        if request.method == 'POST':
            if request.user.is_authenticated:
                if request.user.id == id:
                    create_post_user(request)
                    return render(request, 'frontend/html/user.html', context={'user_profile': user[0], 'posts': posts})

    return HttpResponseRedirect('/')

def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'frontend/html/create_post.html', context={'recaptcha': FormWithCaptcha})

        if request.method == 'POST':
            create_thread(request)

    return HttpResponseRedirect('/')

def thread(request, id):
    post = Post.objects.get(id=id)
    post_user = User.objects.get(id=post.id_creator)

    if request.method == 'GET':
        comment_user = get_comments(request, id)
        return render(request, 'frontend/html/thread.html', context={'post':post_user, 'comment': comment_user, 'info_post': post})

    if request.method == 'POST':
        if request.user.is_authenticated:
            create = create_comment(request, id)
            if create == True:
                comment_user = get_comments(request, id)
                return render(request, 'frontend/html/thread.html', context={'post':post_user, 'comment': comment_user, 'info_post': post})

    return HttpResponseRedirect('/')

def logout(request):
    if request.user.is_authenticated:
        logout_user(request)
    
    return HttpResponseRedirect('/')

def change_photo(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            change_user_photo(request, request.user.id)
            return HttpResponseRedirect(f'/user/{request.user.id}')

    return HttpResponseRedirect('/')
