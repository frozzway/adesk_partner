# Generated by Django 4.0.5 on 2022-06-21 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0010_partner_debt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='INN',
            field=models.CharField(max_length=32, verbose_name='ИНН'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='commission',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='Процент комисии'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='company_name',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='Наименование компании'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='contract_number',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Номер договора'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='date_registered',
            field=models.DateTimeField(null=True, verbose_name='Дата подачи заявки'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='debt',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Задолженность'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='first_name',
            field=models.CharField(max_length=32, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='last_name',
            field=models.CharField(max_length=32, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='partner',
            name='phone_number',
            field=models.CharField(max_length=32, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_activated',
            field=models.DateTimeField(null=True, verbose_name='Дата активации'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Активирован'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Полномочия администратора'),
        ),
    ]
