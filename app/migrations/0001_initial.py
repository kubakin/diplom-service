# Generated by Django 3.1.2 on 2020-10-10 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True, verbose_name='Дата действия')),
                ('action', models.TextField(verbose_name='Действие')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('historyOfUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.history', verbose_name='История пользователя')),
            ],
        ),
    ]
