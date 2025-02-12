from django.http import HttpResponse

# Imports the model for users (built into django)
from django.contrib.auth.models import User

# GETS ALL USER INFORMATION
def get_all_user_info(request):
    all_users = User.objects.all()
    return HttpResponse(all_users)

# GETS JUST A SINGLE USERS DATA
def get_just_dude(request):
    user_info = User.objects.get(username='dude')
    print(
        user_info.id)  # NOW WE CAN ACCESS SPECIFIC INFORMATION ABOUT THE USER FROM HERE (specific elements defined in the object)
    return HttpResponse(user_info)


# Imports our custom topic item
from .models import Topic


# CREATES TOPICS
def create_topics(request):
    user = User.objects.get(username='dude')
    Topic.objects.create(author=user, name='Epic')
    Topic.objects.create(author=user, name='Gnarly')
    Topic.objects.create(author=user, name='Awesome')
    return HttpResponse('topics made!')


# FILTER THE RESULTS YOU GET
def filter_for_something(request):
    user = User.objects.get(username='dude')
    results = Topic.objects.filter(author=user)
    return HttpResponse(results)


