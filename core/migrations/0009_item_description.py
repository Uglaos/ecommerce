# Generated by Django 3.0.6 on 2020-05-23 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='This is a test description'),
            preserve_default=False,
        ),
    ]
