# Generated by Django 3.1.7 on 2021-11-30 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='product',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
