# Generated by Django 4.0.3 on 2022-05-05 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webexample', '0006_pets_photos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pets',
            name='photos',
        ),
    ]
