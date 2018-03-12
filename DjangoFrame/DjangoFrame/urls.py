"""DjangoFrame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

# 定义每次请求的URL和响应函数
urlpatterns = [
    path('admin/', admin.site.urls),
    # 使用正则,表示所有空请求,设置根域名显示页面
    path(r'^$',blog.views.showBlogList),
    #
    path(r'^blog/(d+)$',blog.views.showBlog)
]