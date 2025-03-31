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