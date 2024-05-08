# Generated by Django 5.0.4 on 2024-05-06 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_remove_goal_image_remove_goal_reflection'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='image',
            field=models.ImageField(blank=True, upload_to='goal_images/'),
        ),
        migrations.AddField(
            model_name='goal',
            name='reflection',
            field=models.TextField(blank=True),
        ),
    ]