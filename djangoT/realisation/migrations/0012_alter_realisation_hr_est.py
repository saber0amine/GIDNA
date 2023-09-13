# Generated by Django 4.2.4 on 2023-09-01 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planification', '0010_alter_planification_nature'),
        ('realisation', '0011_alter_realisation_emplacement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realisation',
            name='hr_est',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heures_estimee', to='planification.planification'),
        ),
    ]