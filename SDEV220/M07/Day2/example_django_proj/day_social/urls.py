from django.urls import path
from . import views
from . import inserts


from django.contrib.auth import views as l_views

urlpatterns = [
    # Main Page
    path('', views.main_page),

    # Topics page
    path('topics/<int:id>', views.topic_page),


    # Insert Test Data
    path('insert', inserts.insert_everything),
    path('insert/ignore', inserts.insert_everything_ignore),

    # Making Posts
    path('make/post', views.make_post),
    path('make/topic', views.make_topic),

    # Account Paths
    path('account', views.account_page),
    path('accounts/login/', l_views.LoginView.as_view(), name='login'),
    path("signup/", views.SignUpView.as_view(), name="signup"),

]
