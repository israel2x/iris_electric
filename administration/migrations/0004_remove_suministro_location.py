# Generated by Django 3.0.7 on 2021-07-26 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_suministro_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='suministro',
            name='location',
        ),
    ]