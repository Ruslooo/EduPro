from django.urls import path

from .views import *

app_name = 'posts'

urlpatterns = [
    path('addpage/', AddPage.as_view(), name='add_page'),

    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path("post/<slug:post_slug>/leave_like", PostHome.leave_like, name="leave_like"),
    path("post/<slug:post_slug>/leave_dislike", PostHome.leave_dislike, name="leave_dislike"),
    path('comment/post/<slug:post_slug>/add_comment/', add_comment, name='add_comment'),
    # path('post/<slug:post_slug>/', , name='post')
]