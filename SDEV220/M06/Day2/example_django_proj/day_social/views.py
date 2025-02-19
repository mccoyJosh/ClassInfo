from django.shortcuts import render
from .models import Post
from .models import Topic


def main_page(request):
    posts = Post.objects.all().order_by('-epic_value')[:35]
    return render(request, 'main_posts.html', {
        'posts': posts
    })


def topic_page(request, id):
    topic = Topic.objects.get(id=id)
    posts = Post.objects.all().filter(topic=topic).order_by('-epic_value')

    return render(request, 'topic.html', {
        'posts': posts,
        'topic': topic.name,
    })
