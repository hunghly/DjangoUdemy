# Generated by Django 3.1 on 2020-08-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='book',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
