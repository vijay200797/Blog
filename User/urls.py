from django.urls import path
from User.views import (    
    vw_ViewUsers,
    vw_RegisterUser,
    vw_LoginUser,
    vw_ForgetUserID
    )

urlpatterns = [
    path('', vw_ViewUsers),
    path('create/', vw_RegisterUser),
    path('login/', vw_LoginUser),
    path('forget/', vw_ForgetUserID),
]