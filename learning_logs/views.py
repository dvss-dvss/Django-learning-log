from django.shortcuts import redirect, render

from .models import Topic
from .forms import TopicForm

# Create your views here.

def index(request):
    """Головна сторінка застосунку"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Виводе список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Виводе одну тему та всі її дописи"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries,
    }
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Додає нову тему"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
