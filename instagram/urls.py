"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth.views import LogoutView
from posts.views import index, create_post, update_post, single_post
from users.views import register, signin, account, edit_profile, followers, follows

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name="index"),
    path('register/', register, name = 'register'),
    path('login/', signin, name='login' ),
    path('logout/', LogoutView.as_view(next_page = 'index'), name='logout'),
    path('create_post/', create_post, name = 'create_post'),
    path('update_post/<int:id>/', update_post, name = 'update_post'),
    path('single_post/<int:id>/', single_post, name = 'single_post'),
    path('account/<int:id>/', account, name = 'account'),
    path('edit_profile/<int:id>/', edit_profile, name = 'edit_profile'),
    path('account/followers/<int:id>/', followers, name='followers'),
    path('account/follows/<int:id>/', follows, name='follows'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
