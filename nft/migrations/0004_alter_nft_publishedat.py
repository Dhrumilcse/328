# Generated by Django 3.2 on 2021-04-30 05:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0003_nft_publishedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nft',
            name='publishedAt',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
