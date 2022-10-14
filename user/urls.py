from django.urls import path
from .views import get_all_users, insert_user

urlpatterns = [
    path('all',get_all_users),
    path('add',insert_user),
]