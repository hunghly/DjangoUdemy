# Generated by Django 3.1 on 2020-08-09 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=36, null=True, unique=True)),
                ('genre', models.CharField(choices=[('AC', 'Action'), ('FAN', 'Fantasy'), ('NF', 'Non-fiction'), ('FC', 'Fiction')], max_length=50)),
                ('kid_friendly', models.CharField(blank=True, choices=[('KF', 'Kid-Friendly'), ('NKF', 'Not-Kid-Friendly')], max_length=50)),
                ('status', models.IntegerField(choices=[(0, 'Unknown'), (1, 'processed'), (2, 'paid')], null=True)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
            ],
        ),
    ]