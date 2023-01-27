from django.urls import path
from user import views as v

urlpatterns = [
    path('add/', v.insert_user),
    path('login/', v.login_user),
    path('logout/', v.logout_user),
    path('me/', v.get_user),
    path('changepassword/', v.change_password),
]
