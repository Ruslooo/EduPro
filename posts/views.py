from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse, Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, DetailView

from comments.forms import CommentForm
from comments.models import Comment
from posts.forms import AddPostForm
from posts.models import *

menu = [
    {'title': "Добавить пост", 'url_name': 'posts:add_page'},
]


class PostHome(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(is_published=True)
        context["title"] = 'Главная страница'
        context["menu"] = menu
        return context

    def handle_no_permission(self):
        return redirect('profiles:login')

    @staticmethod
    def leave_like(request, *args, **kwargs):
        try:
            instance = get_object_or_404(Post, slug=kwargs.get("post_slug"))
            instance.likes_count += 1
            instance.save()
            return JsonResponse({"status": True, "message": "Вы поставили лайк"})
        except Http404:
            return JsonResponse({"status": False, "message": "Пост не был найден"})

    @staticmethod
    def leave_dislike(request, *args, **kwargs):
        try:
            instance = get_object_or_404(Post, slug=kwargs.get("post_slug"))
            instance.dislikes_count += 1
            instance.save()
            return JsonResponse({"status": True, "message": "Вы поставили лайк"})
        except Http404:
            return JsonResponse({"status": False, "message": "Пост не был найден"})

class AddPage(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'posts/addpage.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.department = self.request.user.department
        post.save()
        return super().form_valid(form)

class ShowPost(DetailView):
    model = Post
    template_name = 'posts/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("show-post", kwargs={'post_slug': post.slug}))
        else:
            return self.get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comment.objects.filter(post=post)
        post_comments_count = Comment.objects.filter(post=post).count()
        context.update({
            'form': CommentForm(),
            'comments': comments,
            'post_comments_count': post_comments_count,
        })
        return context

@login_required
@require_http_methods(["POST"])
def add_comment(request, *args, **kwargs):

    form = CommentForm(request.POST)
    post = get_object_or_404(Post, slug=kwargs.get("post_slug"))

    if form.is_valid():
        comment = Comment()
        comment.post = post
        comment.author = auth.get_user(request)
        comment.content = form.cleaned_data['content']
        comment.save()

    return redirect(post.get_absolute_url())
