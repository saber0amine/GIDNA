# Generated by Django 4.2.4 on 2023-08-21 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planification', '0003_alter_planification_my_objrctif'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planification',
            old_name='my_objrctif',
            new_name='my_objectif',
        ),
    ]
