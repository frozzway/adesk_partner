# Generated by Django 4.0.5 on 2022-06-09 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0002_partner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='user_id',
            new_name='user',
        ),
    ]
