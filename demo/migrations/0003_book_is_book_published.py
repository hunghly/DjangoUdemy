# Generated by Django 3.1 on 2020-08-09 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20200809_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_book_published',
            field=models.BooleanField(default=False),
        ),
    ]