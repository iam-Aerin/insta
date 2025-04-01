from django.db import models
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField
# Create your models here.
class User(AbstractUser):
    profile_image = ResizedImageField(
        size=[500, 500],
        crop=['middle', 'center'],
        upload_to='profile'    
    )
    
    # User와 Post는 1:N관계로 Foreign Key로 연결되어있다. 
    # django는 우리 모르게 자동으로 post_set (FK) 을 만들고 있었다.
    
    # 이외에도 Comment_set이 저장되는 중이었음.
    # 그리고 좋아요 기능을 위해 post와 user를 다시 연결 시키려고함.
    # 그때 post_set이 다시 생기는데, 이때 이름 설정을 (related_name을 post_set이 아닌
    # 다른 이름으로 설정을 해줘야 충돌이 일어나지 않음
    
    # 그래서, `models.py` 에서는 `related_name = 'like_posts' 로 설정하면
    # N:M 관계의 like_posts(MMF) 가 탄생함. 
    
    # => db에 posts_post_like_user라는 테이블이 생김. (user_id와 post_id를 저장함)
