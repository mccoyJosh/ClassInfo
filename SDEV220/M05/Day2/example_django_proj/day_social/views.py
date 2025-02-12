from django.shortcuts import render


def t_page(request):
    return render(request, 't.html', {})


def simple_html_page(request):
    return render(request, 'simple.html', {})


def main_page(request):
    return render(request, 'main_page.html', {})
