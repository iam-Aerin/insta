# 새로 만듦 create form을 위해서

from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta():
        model = Post
        fields = '__all__'