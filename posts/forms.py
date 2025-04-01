# 새로 만듦 create form을 위해서

from django.forms import ModelForm
from .models import Post, Comment

class PostForm(ModelForm):
    class Meta():
        model = Post
        # fields = '__all__'
        fields = ('content', 'image',)
        

 # 댓글 작성
class CommentForm(ModelForm):
     class Meta():
         model = Comment
         fields = ('content',)
         # fields = ('content', 'image',)
         
         
#  # 댓글 수정
#  class CommentUpdateForm(ModelForm):
#      class Meta():
#          model = Comment
#          fields = ('content',)
#          # fields = ('content', 'image',)
         
         
#  # 댓글 삭제
#  class CommentDeleteForm(ModelForm):
#      class Meta():
#          model = Comment
#          fields = ('content',)
        