# Generated by Django 2.0.2 on 2019-01-20 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20190103_0411'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total',
        ),
    ]