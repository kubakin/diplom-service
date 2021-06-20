# Generated by Django 3.1.2 on 2021-04-18 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_sitereport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestData',
        ),
        migrations.AlterField(
            model_name='sitereport',
            name='cnt',
            field=models.IntegerField(verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='sitereport',
            name='data',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата отчета'),
        ),
        migrations.AlterField(
            model_name='sitereport',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.site'),
        ),
        migrations.AlterModelTable(
            name='sitereport',
            table='app_sitereport',
        ),
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
