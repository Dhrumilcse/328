# Generated by Django 3.2 on 2021-04-30 05:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0002_nft_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='nft',
            name='publishedAt',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 30, 5, 8, 30, 8727)),
        ),
    ]
