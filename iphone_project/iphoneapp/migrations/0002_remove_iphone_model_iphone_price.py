# Generated by Django 4.2.5 on 2023-09-29 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iphoneapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iphone',
            name='model',
        ),
        migrations.AddField(
            model_name='iphone',
            name='price',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
