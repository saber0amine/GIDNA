# Generated by Django 4.2.4 on 2023-08-21 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planification', '0004_rename_my_objrctif_planification_my_objectif'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planification',
            name='my_objectif',
        ),
    ]