# insta project 만들기


posts: app name 설정


```shell
박수똥@DESKTOP-P724I6Q MINGW64 ~/Desktop/DAMF2/insta (master)
$ python manage.py makemigrations
SystemCheckError: System check identified some issues:

ERRORS:
posts.Post.image: (fields.E210) Cannot use ImageField because Pillow is not installed.
        HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".
```

`ImageField`를 사용하려면 `python -m pip install Pillow`

image폴더가 생성됨
> 그 폴더 또한  .gitignore에 포함한다. 
- 마지막 줄에 `image/`를 추가해 .gitignore 파일을 수정했다. 

만일 이 파일을 다시 clone 해서 쓸 때 어떤 라이브러리들이 필요한지를 알려주도록
```shell
pip freeze >> requirements.txt
```
> 코드를 작성하다가 새로운 라이브러리가 추가된 상황이라면 그때 또 다시 위 코드로 업데이트를 시켜줘야함. 

데이터 베이스가 이미지를 직접 저장하는게 아니라 그 이미지 파일의 경로를 저장한다. 
`Media Root` 설정
`Media URL` 
`settings.py` 에서 

```shell
> django resized
: pip install django-resized
> django 부트스트랩 적용시키기
: pip install django-bootstrap5
```