# Generated by Django 4.2.4 on 2023-09-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objectif', '0010_objectif_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectif',
            name='date_objectif',
            field=models.DateField(null=True),
        ),
    ]
