# Generated by Django 4.1.3 on 2022-11-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.TextField(default='this is cool!'),
        ),
    ]
