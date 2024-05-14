from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class FeedBack(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='feedbacks', verbose_name='Автор')
    email = models.EmailField(verbose_name='Почта')
    message = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.author} отзыв'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
    