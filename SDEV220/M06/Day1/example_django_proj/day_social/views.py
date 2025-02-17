from django.shortcuts import render
from  .models import Post

def main_page(request):
    posts = Post.objects.all().order_by('-epic_value')[:35]
    return render(request, 'main_page.html', {'posts':posts})


def main_but_boot(request):
    posts = Post.objects.all().order_by('-epic_value')[:35]
    return render(request, 'bootstrap.html', {'posts':posts})


def main_but_extending(request):
    posts = Post.objects.all().order_by('-epic_value')[:35]
    return render(request, 'post_list.html', {'posts':posts})


def simple_show_template_tag_page(request):
    first_post = Post.objects.first()
    return render(request, 'simple_tag.html', {'post':first_post})

def simple_css_page_1(request):
    return render(request, 'css_1/simple_css.html', {})

def simple_css_page_2(request):
    return render(request, 'css_2/simple_css.html', {})

def simple_css_page_3(request):
    return render(request, 'css_3/simple_css.html', {})

