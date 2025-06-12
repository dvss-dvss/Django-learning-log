from django.db import models

# Create your models here.

class Topic(models.Model):
    """Тема, яку вивчає користувач."""

    text = models.CharField(max_length=255, verbose_name='Назва теми')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Створено')

    def __str__(self):
        return self.text