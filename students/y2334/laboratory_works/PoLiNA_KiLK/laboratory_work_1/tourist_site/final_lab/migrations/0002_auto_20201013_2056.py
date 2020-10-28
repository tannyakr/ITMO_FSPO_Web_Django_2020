# Generated by Django 3.1.2 on 2020-10-13 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('final_lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ways',
            name='Name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='name', to='final_lab.routes'),
        ),
        migrations.AlterField(
            model_name='ways',
            name='Number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='number', to='final_lab.buses'),
        ),
    ]