# Generated by Django 3.0.5 on 2020-04-21 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=32, verbose_name='Марка')),
                ('model', models.CharField(max_length=32, verbose_name='Модель')),
                ('color', models.CharField(max_length=32, verbose_name='Цвет')),
                ('num', models.CharField(max_length=32, verbose_name='Гос. номер')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='Имя владельца')),
                ('last_name', models.CharField(max_length=48, verbose_name='Фамилия владельца')),
                ('birthday', models.DateField(verbose_name='Дата рождения владельца')),
            ],
        ),
        migrations.CreateModel(
            name='OwnerShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('finish', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='cars',
            field=models.ManyToManyField(through='project_first_app.OwnerShip', to='project_first_app.Car'),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, verbose_name='Тип удостоверения')),
                ('issue_date', models.DateField(verbose_name='Дата получение')),
                ('expiration_date', models.DateField(null=True, verbose_name='Дата окончания')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
    ]
