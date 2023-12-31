# Generated by Django 4.2.4 on 2023-08-21 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('objectif', '0005_rename_my_objectif_objectif_obj'),
        ('planification', '0008_alter_planification_obj'),
        ('realisation', '0002_rename_date_creation_realisation_date_realisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='realisation',
            name='obj',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='objectif.objectif'),
        ),
        migrations.AddField(
            model_name='realisation',
            name='tache',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='planification.planification'),
        ),
    ]
