from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    posts = Post.objects.all()
    form = CommentForm()
    
    context = {
        'posts' : posts,
        'form' : form,
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

# Comment Create 함수
@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post_id = post_id
        comment.save()
        
        return redirect('posts:index')
    # else:
    #     return redirect('posts:index')
    
# Like 함수 구현하기 (게시물 관점으로)
# def like(request, post_id):
#     user = request.user
#     post = Post.objects.get(id=post_id)
    
#     if post in user.like_posts.all:
#         user.like_posts.remove(post)
#     else:
#         user.like_posts.add(post)
        
#     return redirect('posts:index')

# Like 함수 구현하기 (user 관점으로)
@login_required
def like(request, post_id):
    user = request.user
    post = Post.objects.get(id=post_id)
    
    if user in post.like_users.all():
        post.like_users.remove(user)
    else:
        post.like_users.add(user)
        
    return redirect('posts:index')


