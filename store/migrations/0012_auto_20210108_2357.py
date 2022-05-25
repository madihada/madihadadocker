# Generated by Django 2.2 on 2021-01-08 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_orderitem_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='price',
        ),
        migrations.AddField(
            model_name='orderitem2',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]