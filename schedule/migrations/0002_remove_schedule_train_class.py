# Generated by Django 3.2.9 on 2023-08-30 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='train_class',
        ),
    ]
