# Generated by Django 4.2.15 on 2024-09-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='docresinterno',
            options={'verbose_name': 'Documento de resultado de examen interno', 'verbose_name_plural': 'Documentos de resultados de exámenes internos'},
        ),
        migrations.AlterModelOptions(
            name='docreslaboratorio',
            options={'verbose_name': 'Documento de resultado de examen laboratorio', 'verbose_name_plural': 'Documentos de resultados de exámenes laboratorio'},
        ),
        migrations.AlterModelOptions(
            name='exinterno',
            options={'verbose_name': 'Examen interno', 'verbose_name_plural': 'Exámenes internos'},
        ),
        migrations.AlterModelOptions(
            name='exlaboratorio',
            options={'verbose_name': 'Examen de laboratorio', 'verbose_name_plural': 'Exámenes de laboratorio'},
        ),
        migrations.AlterField(
            model_name='exlaboratorio',
            name='nombrelab',
            field=models.CharField(blank=True, db_column='nombrelab', max_length=80, null=True, verbose_name='Nombre del laboratorio'),
        ),
    ]
