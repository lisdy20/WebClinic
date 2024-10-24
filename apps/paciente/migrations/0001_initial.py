# Generated by Django 4.2.15 on 2024-09-14 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_column='nombre', max_length=30, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, db_column='apellido', max_length=30, null=True, verbose_name='Apellido')),
                ('dpi', models.CharField(blank=True, db_column='dpi', max_length=14, null=True, verbose_name='DPI')),
                ('nit', models.CharField(blank=True, db_column='nit', max_length=10, null=True, verbose_name='NIT')),
                ('direccion', models.CharField(blank=True, db_column='direccion', max_length=30, null=True, verbose_name='Dirección')),
                ('fechanac', models.DateField(blank=True, db_column='fechanac', null=True, verbose_name='Fecha de Nacimiento')),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], db_column='genero', max_length=1, null=True, verbose_name='Género')),
                ('telefono', models.CharField(blank=True, db_column='telefono', max_length=15, null=True, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
                'db_table': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='TipoAntecedente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_column='nombre', max_length=30, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Tipo de Antecedente',
                'verbose_name_plural': 'Tipo de Antecedentes',
                'db_table': 'TipoAntecedente',
            },
        ),
        migrations.CreateModel(
            name='ContactoPaciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numcel', models.CharField(blank=True, db_column='numcel', max_length=15, null=True, verbose_name='Número de celular')),
                ('numcasa', models.CharField(blank=True, db_column='numcasa', max_length=15, null=True, verbose_name='Número de casa')),
                ('contactoemergencia', models.BooleanField(db_column='contactoemergencia', default=False, verbose_name='Contacto de emergencia')),
                ('paciente', models.ForeignKey(db_column='paciente_id', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Contacto Paciente',
                'verbose_name_plural': 'Contactos Pacientes',
                'db_table': 'contactopaciente',
            },
        ),
        migrations.CreateModel(
            name='Antecedente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(db_column='descripcion', max_length=255, verbose_name='Descripción')),
                ('paciente', models.ForeignKey(db_column='paciente', on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente', verbose_name='Paciente')),
                ('tipoantecedente', models.ForeignKey(db_column='tipoantecedente', on_delete=django.db.models.deletion.CASCADE, to='paciente.tipoantecedente', verbose_name='Tipo de Antecedente')),
            ],
            options={
                'verbose_name': 'Antecedente',
                'verbose_name_plural': 'Antecedentes',
                'db_table': 'antecedentes',
            },
        ),
    ]
