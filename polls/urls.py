from django.urls import path
### django의 urls 모듈에서 path 메소드를 가져다가 쓰겠다는 뜻
from . import views
### 이때 .은 현재 패키지(polls)에서 라는 뜻으로 현재 패키지의 views를 임포트 한다는 것

urlpatterns = [
    path('', views.index, name='index')
]
### path 매소드 '패키지 명 뒤에 올 경로', 뷰에서 불러올 것, 뷰의 이름