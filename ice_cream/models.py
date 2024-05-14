from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill


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
    

    def get_first_image(self):
        if self.images:
            return self.images.first().image.url
        else:
            return 


class Image(models.Model):
    ice_cream = models.ForeignKey(IceCream, on_delete=models.CASCADE, related_name='images')

    image = ProcessedImageField(
        upload_to='product_images/',
        processors=[ResizeToFill(800, 600)],
        format='JPEG',
        options={'quality': 90}
    )
    thumbnail = ImageSpecField(
        source='image',
        processors=[ResizeToFill(300, 300)],
        format='JPEG',
        options={'quality': 70}
    )