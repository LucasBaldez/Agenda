# Generated by Django 3.1.3 on 2020-11-20 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostrar',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='data_criacao',
            field=models.DateTimeField(),
        ),
    ]
