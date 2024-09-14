# Generated by Django 4.2.15 on 2024-09-14 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinica', '0002_alter_cita_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExLaboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(db_column='motivo', max_length=80, verbose_name='Motivo del examen')),
                ('nombrelab', models.CharField(blank=True, db_column='nombrelab', max_length=80, null=True, verbose_name='Nombre del Laboratorio')),
                ('cita', models.ForeignKey(db_column='cita', on_delete=django.db.models.deletion.CASCADE, to='clinica.cita', verbose_name='Cita')),
            ],
            options={
                'verbose_name': 'Examen de Laboratorio',
                'verbose_name_plural': 'Exámenes de Laboratorio',
                'db_table': 'ExLaboratorio',
            },
        ),
        migrations.CreateModel(
            name='ExInterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.CharField(db_column='motivo', max_length=80, verbose_name='Motivo del examen')),
                ('nombredoctor', models.CharField(blank=True, db_column='nombredoc', max_length=80, null=True, verbose_name='Doctor que realiza examen')),
                ('detallecita', models.ForeignKey(db_column='detallecita', on_delete=django.db.models.deletion.CASCADE, to='clinica.detallecita', verbose_name='Cita')),
            ],
            options={
                'verbose_name': 'Examen Interno',
                'verbose_name_plural': 'Exámenes Internos',
                'db_table': 'ExInterno',
            },
        ),
        migrations.CreateModel(
            name='DocResLaboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=30, verbose_name='Nombre del documento')),
                ('ubicacion', models.FileField(db_column='ubicacion', upload_to='', verbose_name='Ubicación')),
                ('exlaboratorio', models.ForeignKey(db_column='exlaboratorio_id', on_delete=django.db.models.deletion.CASCADE, to='examenes.exlaboratorio', verbose_name='Examen de laboratorio')),
            ],
            options={
                'verbose_name': 'Documento de Resultado de Examen Laboratorio',
                'verbose_name_plural': 'Documentos de Resultados de Exámenes Laboratorio',
                'db_table': 'DocResLaboratorio',
            },
        ),
        migrations.CreateModel(
            name='DocResInterno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=30, verbose_name='Nombre del documento')),
                ('ubicacion', models.FileField(db_column='ubicacion', upload_to='', verbose_name='Ubicación')),
                ('exinterno', models.ForeignKey(db_column='exinterno_id', on_delete=django.db.models.deletion.CASCADE, to='examenes.exinterno', verbose_name='Examen interno')),
            ],
            options={
                'verbose_name': 'Documento de Resultado de Examen Interno',
                'verbose_name_plural': 'Documentos de Resultados de Exámenes Internos',
                'db_table': 'DocResInterno',
            },
        ),
    ]
