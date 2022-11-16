from django.shortcuts import get_object_or_404, render
from .models import Group, Post
POST_LIMIT = 10


def index(request):
    posts = Post.objects.all().select_related('author')[:POST_LIMIT]
    title = 'Последние обновления на сайте',
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all().select_related('author')[:POST_LIMIT]
    title = 'Записи сообщества Лев Толстой – зеркало русской революции.'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, 'posts/group_list.html', context)
