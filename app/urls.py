from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('search/', views.load_suggestion, name='load_suggestion'),
    path('article/display/', views.get_article, name='get_article')
]
