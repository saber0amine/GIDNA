# Generated by Django 4.2.4 on 2023-08-26 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_remove_login_projet'),
        ('lists', '0008_remove_lists_date_creation_remove_lists_name_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lists',
            name='name_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='login.login'),
        ),
        migrations.AlterField(
            model_name='emplacement',
            name='emplacement',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='lists',
            name='emplacement',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
