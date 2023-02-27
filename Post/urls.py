from django.urls import path

from .views import (    
    vw_ViewPost,
    vw_CreatePost,
    vw_DeletePost,
    )

urlpatterns = [
    path('', vw_ViewPost, name='viewPost'),
    path('create/', vw_CreatePost, name='createPost'),
    path('delete/<int:id>', vw_DeletePost, name='deletePost')
]



'''
from Post import views



urlpatterns  = [
    path(r'^/', views.vw_ViewPost),
    path(r'^first/', views.vw_CreatePost)
]
'''