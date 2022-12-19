from django.urls import path
from User.views import (    
    vw_ViewUsers,
    vw_RegisterUser,
    vw_LoginUser,
    vw_ForgetUserID,
    vw_LogOutUser
    )

urlpatterns = [
    path('', vw_ViewUsers),
    path('create/', vw_RegisterUser, name='signup'),
    path('login/', vw_LoginUser, name='login'),
    path('forget/', vw_ForgetUserID, name='forget'),
    path('logout/', vw_LogOutUser, name='logout'),
]