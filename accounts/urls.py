from django.urls import path, include

from . import views

app_name = 'accounts'
urlpatterns = [
    # Додати URL авторизації за замовчуванням
    path('', include('django.contrib.auth.urls')),
    # Сторінка реєстрації
    path('register/', views.register, name='register'),
]

