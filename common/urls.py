from django.urls import path
from posts.views import *

app_name = 'common'

urlpatterns = [
    path('', PostHome.as_view(), name='home')
]