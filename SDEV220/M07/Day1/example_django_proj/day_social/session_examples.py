from django.shortcuts import render


def set_blue(request):
    request.session['color'] = 'blue'
    info = 'Your color is now blue!'
    return render(request, 'show_stuff.html', {"info": info})


def set_red(request):
    request.session['color'] = 'red'
    info = 'Your color is now red!'
    return render(request, 'show_stuff.html', {"info": info})


def get_color(request):
    found_color = 'NONE'
    if 'color' in request.session:
        found_color = request.session['color']

    info = f"Here is your color: {found_color}"
    return render(request, 'show_stuff.html', {'info': info})
