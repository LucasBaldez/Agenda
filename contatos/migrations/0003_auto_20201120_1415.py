# Generated by Django 3.1.3 on 2020-11-20 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_auto_20201120_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='mostrar',
            new_name='ativo',
        ),
    ]
