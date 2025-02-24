from django.urls import path
from . import views
from . import inserts
from . import session_examples


from django.contrib.auth import views as l_views

urlpatterns = [
    path('', views.main_page),
    path('topics/<int:id>', views.topic_page),
    path('insert', inserts.insert_everything),
    path('insert/ignore', inserts.insert_everything_ignore),
    path('make/post', views.make_post),
    path('make/topic', views.make_topic),
    path('account', views.account_page),

    path('accounts/login/', l_views.LoginView.as_view(), name='login'),
    path("signup/", views.SignUpView.as_view(), name="signup"),

    # Session Example
    path('setblue', session_examples.set_blue),
    path('setred', session_examples.set_red),
    path('color', session_examples.get_color),
]
