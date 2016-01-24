"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin

# 教程中的这个项目只有一个应用polls。
# 在真实的Django项目中，可能会有五个、十个、二十个或者更多的应用。
# Django如何区分它们URL的名字呢？
# 例如，polls 应用具有一个detail 视图，相同项目中的博客应用可能也有这样一个视图。
# 当使用模板标签{% url %}时，人们该如何做才能使得Django知道为一个URL创建哪个应用的视图？
# 答案是在你的主URLconf下添加命名空间。
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^polls/', include('polls.urls', namespace='polls')),
]
