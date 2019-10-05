"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, re_path, include
from blog.views import(
    blog_post_create_view,
)
from .views import(
    home,
    contact,
    about
)

urlpatterns = [
    path('',home),
    # path('blog/',blog_post_detail_page),
    # path('blog/<int:post_id>/',blog_post_detail_page),
    path('create_blog/',blog_post_create_view),
    path('blog/',include('blog.urls')),
    # re_path(r'blog/(?P<post_id>\d+)/$', blog_post_detail_page),
    path('contact/',contact),
    path('about/',about),
    path('nt1_place/', admin.site.urls),
]
