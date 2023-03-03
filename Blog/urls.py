"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from BlogApp.views import (    
    home_screen_veiw, vw_Upload, vw_Files
    )

from Post.views import (    
    vw_CreatePost,
    vw_ViewPost
    )

from User.views import (    
    vw_ViewUsers,
    vw_RegisterUser,
    vw_LoginUser,
    vw_ForgetUserID
    )

urlpatterns = [
    path('', home_screen_veiw),
    path('upload', vw_Upload),
    path('files', vw_Files),
    path('admin/', admin.site.urls),
    path('user/', include("User.urls")),
    path('post/', include("Post.urls"), name='post'),
    path('shops/', include("shops.urls"), name='shops'),
    path('api/', include("API.urls"), name='api'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)