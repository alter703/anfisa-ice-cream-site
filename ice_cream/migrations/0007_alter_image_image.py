# Generated by Django 5.0.6 on 2024-05-14 11:15

import imagekit.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0006_remove_icecream_image_image_ice_cream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='product_images/'),
        ),
    ]
