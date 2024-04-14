from django.shortcuts import render,redirect
from .form import RegisterForm,PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from .models import Post

# Create your views here.
@login_required(login_url='login')
def Home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        #taking the id i passed in value attribute
        post_id = request.POST.get("post_id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.auther == request.user:
            post.delete()
    return render(request,"main/home.html", {"posts":posts})


def Update_post(request,pk):
    page = "update"
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.auther = request.user
            post.save()
            return redirect('home')
    return render(request,'main/create_post.html',{"form":form,"page":page})




 
def Registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
        
    else:
        form = RegisterForm()
    
        

    return render(request,'registration/register.html', {"form":form})


def Logout(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
def Post_View(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auther = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request,'main/create_post.html',{"form":form})