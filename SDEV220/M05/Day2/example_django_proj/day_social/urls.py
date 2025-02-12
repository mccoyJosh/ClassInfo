from django.urls import path
from . import views
from . import orm_examples
from django.http import HttpResponse

urlpatterns = [
    path('test', lambda response: HttpResponse('You are in the app!'), name='Test'),
    path('simple', views.simple_html_page, name='Simple'),
    path('t', views.t_page),
    path('', views.main_page, name='Main'),

    # Testing ORM!
    path('1', orm_examples.get_all_user_info),
    path('2', orm_examples.get_just_dude),
    path('3', orm_examples.create_topics),
    path('4', orm_examples.filter_for_something),
]
