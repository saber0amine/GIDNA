# Generated by Django 4.2.4 on 2023-08-26 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0009_lists_name_user_alter_emplacement_emplacement_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projet',
            name='name_user',
        ),
    ]