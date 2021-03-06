# Generated by Django 2.0.1 on 2018-01-31 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('try', '0003_auto_20180131_1100'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
