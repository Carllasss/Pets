# Generated by Django 4.0.3 on 2022-05-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webexample', '0007_remove_pets_photos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pets',
            name='photos',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
