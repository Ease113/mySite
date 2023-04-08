"""
URL configuration for mySite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
    ### 최상위 URLconf에서 path를 지정(polls/) -> 127.0.0.1/polls/
    ### 그 후 path(패키지 명)에 따른 경로의 앱들을 연결해준다.
    ### include(polls.urls)는 앞에 polls가 오는 모든 경로의 url에 대하여 polls.urls에서 관리하게 된다.
]
