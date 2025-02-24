from django.shortcuts import render, redirect
from .models import Post, Topic
from django.contrib.auth.models import User
from .forms import TopicForm, PostForm
from django.utils import timezone

####################################################
###############       CREATE USER    ###############
####################################################

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


####################################################
####################################################

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


def make_topic(request):
    if request.method == "POST":
        form = User(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            admin_user = request.user
            topic.author = admin_user
            topic.created_date = timezone.now()
            topic.save()

            this_topic = Topic.objects.get(name=topic.name)
            link = f"/topics/{this_topic.id}"
            return redirect(link, pk=topic.pk)
    else:
        form = TopicForm()
    return render(request, 'make_topic.html', {'form': form})


def account_page(request):
    return render(request, 'account.html', {})

from django.contrib.auth.decorators import login_required

@login_required
def make_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            admin_user = request.user
            post.author = admin_user
            post.epic_value = 1
            post.visible = True
            post.created_date = timezone.now()
            post.save()
            return redirect('/', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'make_post.html', {'form': form})
