# Generated by Django 4.2.15 on 2024-09-14 13:37

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0002_alter_detallerecetame_options_and_more'),
        ('clinica', '0003_alter_cita_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detallecita',
            options={'verbose_name': 'Detalle de cita', 'verbose_name_plural': 'Detalle de citas'},
        ),
        migrations.AlterModelOptions(
            name='estadocita',
            options={'verbose_name': 'Estado de cita', 'verbose_name_plural': 'Estado de citas'},
        ),
        migrations.AlterField(
            model_name='cita',
            name='estadocita',
            field=models.ForeignKey(db_column='estadocita_id', on_delete=django.db.models.deletion.CASCADE, to='clinica.estadocita', verbose_name='Estado de cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='fecha',
            field=models.DateTimeField(db_column='fecha', default=datetime.datetime(2024, 9, 14, 7, 37, 30, 100966), verbose_name='Fecha de cita'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='numserie',
            field=models.CharField(db_column='numserie', max_length=80, verbose_name='Número de serie'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='recetamedica',
            field=models.ForeignKey(db_column='recetamedica_id', on_delete=django.db.models.deletion.CASCADE, to='medicamentos.recetamedica', verbose_name='Receta médica'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='totalpagado',
            field=models.DecimalField(db_column='totalpagado', decimal_places=2, default=0, max_digits=10, verbose_name='Total pagado'),
        ),
        migrations.AlterField(
            model_name='cita',
            name='totalpago',
            field=models.DecimalField(db_column='totalpago', decimal_places=2, default=0, max_digits=10, verbose_name='Total pago'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='frecuenciacard',
            field=models.CharField(blank=True, db_column='frecuenciiacard', max_length=5, null=True, verbose_name='Frecuencia cardíaca'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='frecuenciaresp',
            field=models.CharField(blank=True, db_column='frecuenciaresp', max_length=5, null=True, verbose_name='Frecuencia respiratoria'),
        ),
        migrations.AlterField(
            model_name='historial',
            name='presionarterial',
            field=models.CharField(blank=True, db_column='presionarterial', max_length=20, null=True, verbose_name='Presión arterial'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='costo',
            field=models.DecimalField(db_column='costo', decimal_places=2, max_digits=10, verbose_name='Costo del servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='descripcion',
            field=models.CharField(blank=True, db_column='descripcion', max_length=80, null=True, verbose_name='Descripción del servicio'),
        ),
        migrations.AlterField(
            model_name='servicio',
            name='nombreservicio',
            field=models.CharField(db_column='nombreservicio', max_length=30, verbose_name='Nombre del servicio'),
        ),
    ]