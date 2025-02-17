from django.urls import path
from . import views
from . import inserts

urlpatterns = [
    path('', views.main_page),
    path('insert', inserts.insert_everything),
    path('tag', views.simple_show_template_tag_page),
    path('css1', views.simple_css_page_1),
    path('css2', views.simple_css_page_2),
    path('css3', views.simple_css_page_3),
    path('boot', views.main_but_boot),
    path('extend', views.main_but_extending),
]
