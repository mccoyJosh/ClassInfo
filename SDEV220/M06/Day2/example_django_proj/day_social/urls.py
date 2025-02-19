from django.urls import path
from . import views
from . import inserts

urlpatterns = [
    path('', views.main_page),
    path('topics/<int:id>', views.topic_page),
    path('insert', inserts.insert_everything),
]
