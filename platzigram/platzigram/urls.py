"""platzigram URL Configuration

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
from django.urls import path
from django.conf import settings
from platzigram import views as local_views
from posts import views as posts_views
from django.conf.urls.static import static
from users import views as users_views

urlpatterns = [
    #Los Path definen cuál url es a la que se está esperando responder algo
    path('admin', admin.site.urls),
    path('hello-world', local_views.hello_world, name='hellow_world'),
    path('sorted/', local_views.sort_integers, name='sort'),
    path('hi/<str:name>/<int:age>', local_views.say_hi, name='hi'),
    path('', posts_views.list_posts, name='feed'), 
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup, name='signup'),
    path('users/me/profile/', users_views.update_profile, name='update_profile'),
    path('posts/new/', posts_views.create_posts, name='create_posts'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
