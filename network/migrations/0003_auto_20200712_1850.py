# Generated by Django 3.0.7 on 2020-07-12 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_following_likes_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='time',
            field=models.FloatField(),
        ),
    ]