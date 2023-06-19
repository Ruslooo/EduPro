from django.urls import path

from .views import *

app_name = 'profiles'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path("profile_list/", profile_list, name="profile_list"),
]