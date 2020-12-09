# Generated by Django 3.1.2 on 2020-10-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.CharField(max_length=50, verbose_name='a')),
                ('b', models.CharField(max_length=50, verbose_name='b')),
                ('c', models.CharField(max_length=50, verbose_name='c')),
            ],
        ),
        migrations.AlterField(
            model_name='history',
            name='date',
            field=models.DateField(verbose_name='Дата действия'),
        ),
    ]
