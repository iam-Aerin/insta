from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Post.objects.all()
    
    context = {
        'posts' : posts,
    }
    
    return render(request, 'index.html', context)

# Create 함수
@login_required
# 로그인한 접속자만 create 기능을 쓸 수 있음
def create(request):
    if request.method == 'POST': 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #작성자에 대한 정보를 넣어줘야함
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            return redirect('posts:index')
    else:
        # Get 요청 처리
        form = PostForm()
        
    context = {
        'form' : form, 
    }
    
    return render(request, 'create.html', context)
    