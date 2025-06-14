from django.shortcuts import render

# Create your views here.

def index(request):
    """Головна сторінка застосунку"""
    return render(request, 'learning_logs/index.html')