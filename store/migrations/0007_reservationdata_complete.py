# Generated by Django 2.2 on 2020-07-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_reservationdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationdata',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]