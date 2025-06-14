from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
    # Сторінка зі списком усіх тем
    path('topics/', views.topics, name='topics'),
]