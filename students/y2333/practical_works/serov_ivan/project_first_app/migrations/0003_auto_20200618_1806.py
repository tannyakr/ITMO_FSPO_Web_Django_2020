# Generated by Django 3.0.7 on 2020-06-18 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0002_auto_20200618_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
