# Generated by Django 5.0.6 on 2024-05-14 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0004_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='icecream',
            name='image',
            field=models.ManyToManyField(to='ice_cream.image'),
        ),
    ]
