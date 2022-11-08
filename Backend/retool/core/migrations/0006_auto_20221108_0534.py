# Generated by Django 3.2.12 on 2022-11-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_carro_carroceria_alter_carro_cilindraje_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mantenimiento',
            name='costo',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='descripcion',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='estado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='kilometraje',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='nota',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='mantenimiento',
            name='servicio',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.DeleteModel(
            name='Mantenimiento_Detalle',
        ),
    ]