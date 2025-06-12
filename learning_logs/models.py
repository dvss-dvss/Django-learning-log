from django.db import models

# Create your models here.

class Topic(models.Model):
    """Тема, яку вивчає користувач."""

    text = models.CharField(max_length=255, verbose_name='Назва теми')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'
        

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    """Допис за темами"""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    text = models.TextField(verbose_name='Текст')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    class Meta:
        verbose_name = 'Допис'
        verbose_name_plural = 'Дописи'
        
    def __str__(self):
        return f"{self.text[:50]}..." 