from django.db import models


class IceCream(models.Model):
    name = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    on_main = models.BooleanField('На главную?', default=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)

    class Meta:        
        ordering = ('name',)
        verbose_name = 'мороженое'
        verbose_name_plural = 'мороженое'

    def __str__(self):
        return f'{self.name}'
