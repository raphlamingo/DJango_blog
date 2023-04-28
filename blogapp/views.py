from django.shortcuts import render,redirect
from .models import Users,Posts
from .form import UserForm, PostForm
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def home(request):
    blogs= Posts.objects.all()

    return render(request, 'index.html',{'blog': blogs})

@login_required(login_url='login')
def create_post(request):
    writers= Users.objects.get(user=request.user)
    form= PostForm()
    if request.method == 'POST':
        new_update= PostForm(request.POST)
        if new_update.is_valid():
            new_update.save()
            return redirect('home')

    return render(request, 'make_post.html',{'form':form})


@login_required(login_url='login')
def update(request, pk):
    post= Posts.objects.get(id=pk)
    form= PostForm(instance=post)
    if request.method == 'POST':
        new_update= PostForm(request.POST, instance=post)
        if new_update.is_valid():
            new_update.save()
            return redirect('home')
    return render(request, 'make_post.html', {'form':form})

@login_required(login_url='login')
def delete(request,pk):
    post= Posts.objects.get(id=pk)
    if request.method== "POST":
        post.delete()
        return redirect('home')
    return render( request, 'delete.html')


def read(request, pk):
    post= Posts.objects.get(id=pk)
    return render(request, 'single.html', {'post':post})

def create_user(request):
    form=  UserCreationForm()
    if request.method == 'POST':
        new_user= UserCreationForm(request.POST)
        if new_user.is_valid():
            user= new_user.save()
            login(request, user)
            return redirect('userinfo')

    return render(request, 'new.html',{'form':form})

@login_required(login_url='login')
def about_user(request):
    form= UserForm
    if request.method == 'POST':
        new_user= UserForm(request.POST)
        if new_user.is_valid():
            new_user.save(user=request.user)
            return redirect('home')
        else:
            messages.error(request, 'Username already exist')
    return render(request, 'new.html',{'form':form})

@login_required(login_url='login')
def update_user(request, pk):
    user= User.objects.get(id=pk)
    form= UserForm(instance=user)
    if request.method == 'POST':
        new_user= UserForm(request.POST, instance=user)
        if new_user.is_valid():
            new_user.save()
            return redirect('home')


    return render(request, 'new.html',{'form':form})


def about(request, pk):
    user= Users.objects.get(id=pk)
    posts= Posts.objects.filter(writer=user.id)
    return render(request, 'about.html',{'user':user, 'post':posts} )

def login_user(request):
    if request.method =="POST":
        username= request.POST['username']
        password= request.POST['password']
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')
        user= authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request,'You"re logged in')
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Wrong Username or password')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    logged_user= request.user
    form= Users.objects.get(user=logged_user)
    post= Posts.objects.filter(writer=form.id)
    return render(request,'profile.html',{'user':form, 'post':post})

def find(request):
    search_query= request.GET.get('query')
    writers= Users.objects.filter(first_name__icontains=search_query)
    return render(request,'search.html', {'user':writers })

def result(request,pk):
    writers= Users.objects.get(id=pk)
    posts= Posts.objects.filter(writer=pk)
    return render(request, 'about.html', {'user':writers,'post':posts } )