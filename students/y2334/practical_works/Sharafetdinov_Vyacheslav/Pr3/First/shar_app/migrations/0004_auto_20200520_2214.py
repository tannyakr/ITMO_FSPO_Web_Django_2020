# Generated by Django 3.0.3 on 2020-05-20 19:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shar_app', '0003_auto_20200520_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
