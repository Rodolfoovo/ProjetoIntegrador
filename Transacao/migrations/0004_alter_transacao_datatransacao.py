# Generated by Django 4.2.9 on 2024-07-27 18:47

import Transacao.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transacao', '0003_transacao_horatransacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='dataTransacao',
            field=models.DateField(validators=[Transacao.validators.validate_data_nao_futura]),
        ),
    ]
