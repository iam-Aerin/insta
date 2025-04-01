# app 폴더 안의 urls.py를 수정한 후 추가해준 파일 입니다. 

from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    
    path('<int:post_id>/comments/create/', views.comment_create, name='comment_create'),

]