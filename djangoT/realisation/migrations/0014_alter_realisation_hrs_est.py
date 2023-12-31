# Generated by Django 4.2.4 on 2023-09-01 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planification', '0011_rename_hr_est_planification_hrs_est'),
        ('realisation', '0013_rename_hr_est_realisation_hrs_est'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realisation',
            name='hrs_est',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realisations_hrs_est', to='planification.planification'),
        ),
    ]
