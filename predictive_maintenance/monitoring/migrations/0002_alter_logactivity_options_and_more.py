# Generated by Django 4.2.20 on 2025-03-26 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='logactivity',
            options={'verbose_name': 'Logs Activity', 'verbose_name_plural': 'Logs Aktifitas Pengguna'},
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='tanggal_maintenance',
            field=models.DateField(blank=True, null=True, verbose_name='Tanggal Maintenance'),
        ),
    ]
