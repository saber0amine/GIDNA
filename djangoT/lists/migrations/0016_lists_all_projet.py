# Generated by Django 4.2.4 on 2023-09-06 00:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0015_alter_lists_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lists',
            name='All_projet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lists.projet'),
        ),
    ]
