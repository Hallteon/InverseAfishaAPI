# Generated by Django 3.2.18 on 2023-11-10 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0006_alter_attraction_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='lat',
            field=models.FloatField(default=1, verbose_name='Широта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attraction',
            name='lot',
            field=models.FloatField(default=1.3, verbose_name='Долгота'),
            preserve_default=False,
        ),
    ]