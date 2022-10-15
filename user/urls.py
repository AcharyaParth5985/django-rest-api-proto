from django.urls import path
from .views import get_all_users,insert_user,login_user,logout_user,get_user, change_password

urlpatterns = [
    path('all',get_all_users),
    path('add',insert_user),
    path('login',login_user),
    path('logout',logout_user),
    path('me',get_user),
    path('changepassword', change_password)
]
